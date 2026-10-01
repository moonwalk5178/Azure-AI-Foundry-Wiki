#!/usr/bin/env python3
"""Deterministic maintenance for this repository's OKF wiki. Never edits sources."""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from urllib.parse import unquote, urlsplit
try:
    import yaml
except ImportError:
    sys.exit('Install dependencies: python3 -m pip install -r scripts/requirements.txt')

class UniqueLoader(yaml.SafeLoader):
    pass

def mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, (str, int, float, bool)) or key in result:
            raise ValueError('invalid or duplicate YAML key')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result
UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)

def frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0] != '---':
        return None, text
    try:
        end = lines.index('---', 1)
    except ValueError:
        raise ValueError('unclosed frontmatter')
    data = yaml.load('\n'.join(lines[1:end]), Loader=UniqueLoader)
    if not isinstance(data, dict):
        raise ValueError('frontmatter must be a mapping')
    return data, '\n'.join(lines[end + 1:])

def instant(value):
    if isinstance(value, dt.datetime):
        parsed = value
    else:
        parsed = dt.datetime.fromisoformat(str(value).replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('timestamp must include a timezone')
    return parsed

def atomic(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(dir=path.parent, prefix='.wiki-tool-')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            stream.write(text)
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)

class Wiki:
    def __init__(self, root):
        self.root = root.resolve()
        self.bundle = self.root / 'wiki'
        self.sources = self.root / 'sources'
        self.manifest = self.root / 'maintenance/source-manifest.jsonl'
        self.catalog = self.bundle / 'catalog.jsonl'
        self.issues = []

    def issue(self, level, path, message):
        self.issues.append({'level': level, 'path': str(path.relative_to(self.root)), 'message': message})

    def files(self, base, pattern='*'):
        if not base.is_dir():
            raise ValueError(f'missing directory: {base.name}')
        files = []
        for path in sorted(base.rglob(pattern)):
            if path.is_symlink():
                raise ValueError(f'symlinks are unsupported: {path.relative_to(self.root)}')
            if path.is_file():
                files.append(path)
        return files

    def target(self, origin, resource):
        if not isinstance(resource, str) or not resource.strip():
            raise ValueError('resource must be a non-empty string')
        uri = urlsplit(resource)
        if uri.scheme or resource.startswith('//') or resource.startswith('#'):
            return None
        raw = unquote(uri.path)
        # OKF also permits prose scope descriptors; distinguish explicit paths.
        if not raw or not (raw.startswith(('/', '.')) or '/' in raw or Path(raw).suffix):
            return None
        target = ((self.bundle / raw.lstrip('/')) if raw.startswith('/') else origin.parent / raw).resolve()
        if not target.is_relative_to(self.root):
            raise ValueError('local path escapes repository')
        return target

    def notes(self):
        notes = []
        for path in self.files(self.bundle, '*.md'):
            try:
                text = path.read_text(encoding='utf-8')
                meta, body = frontmatter(text)
                notes.append((path, meta, body))
            except (ValueError, yaml.YAMLError, UnicodeError) as exc:
                self.issue('error', path, str(exc))
        return notes

    def links(self, path, body):
        # Ignore code examples and HTML comments. Parse inline and reference links.
        body = re.sub(r'```.*?```|~~~.*?~~~|<!--.*?-->|`[^`\n]*`', '', body, flags=re.S)
        definitions = dict(re.findall(r'^\s*\[([^\]]+)\]:\s*(\S+)', body, re.M))
        destinations = re.findall(r'\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+["\'][^\n]*?["\'])?\s*\)', body)
        for label, ref in re.findall(r'\[([^\]]+)\]\[([^\]]*)\]', body):
            if (ref or label) in definitions:
                destinations.append(definitions[ref or label])
        for destination in destinations:
            try:
                target = self.target(path, destination.strip('<>'))
                if target:
                    yield target
            except ValueError as exc:
                self.issue('error', path, str(exc))

    def lint(self):
        notes = self.notes()
        incoming = set()
        for path, meta, body in notes:
            reserved = path.name in ('index.md', 'log.md')
            if reserved:
                if meta is not None and (path != self.bundle / 'index.md' or set(meta) != {'okf_version'}):
                    self.issue('error', path, 'reserved index/log frontmatter violates OKF')
                if path == self.bundle / 'index.md' and (not meta or str(meta.get('okf_version')) != '0.2'):
                    self.issue('error', path, 'root index must declare okf_version: "0.2"')
                if path.name == 'log.md':
                    dates = re.findall(r'^## (.+)$', body, re.M)
                    try:
                        parsed = [dt.date.fromisoformat(d) for d in dates]
                        if parsed != sorted(parsed, reverse=True):
                            self.issue('error', path, 'log dates must be newest first')
                    except ValueError:
                        self.issue('error', path, 'log date headings must be YYYY-MM-DD')
                    if re.search(r'^\* ', body.split('\n## ', 1)[0], re.M):
                        self.issue('warning', path, 'log entries precede their first date heading')
            else:
                if not meta or not isinstance(meta.get('type'), str) or not meta['type'].strip():
                    self.issue('error', path, 'concept requires non-empty string type')
                    continue
                if 'tags' in meta and (not isinstance(meta['tags'], list) or not all(isinstance(t, str) for t in meta['tags'])):
                    self.issue('error', path, 'tags must be a list of strings')
                for field in ('generated', 'verified'):
                    if field in meta:
                        actor = meta[field]
                        try:
                            if not isinstance(actor, dict) or not re.fullmatch(r'(?:[^\s/:]+/[^\s]+|human:[^\s]+|process:[^\s]+)', str(actor.get('by', ''))):
                                raise ValueError('invalid actor')
                            instant(actor.get('at'))
                        except (ValueError, TypeError):
                            self.issue('error', path, f'{field} requires actor by and timezone-aware timestamp at')
                if 'generated' not in meta:
                    self.issue('warning', path, 'missing generation provenance')
                if 'stale_after' in meta:
                    try:
                        if instant(meta['stale_after']) <= dt.datetime.now(dt.timezone.utc):
                            self.issue('warning', path, 'stale_after has elapsed')
                    except (ValueError, TypeError):
                        self.issue('error', path, 'invalid stale_after timestamp')
                entries = meta.get('sources', [])
                if not isinstance(entries, list):
                    self.issue('error', path, 'sources must be a list')
                    entries = []
                if not entries and meta['type'] != 'Template':
                    self.issue('warning', path, 'missing sources; review evidence manually')
                ids = set()
                for entry in entries:
                    try:
                        if not isinstance(entry, dict):
                            raise ValueError('source entry must be a mapping')
                        resource = entry.get('resource')
                        target = self.target(path, resource)
                        if target and not target.exists():
                            self.issue('error', path, f'missing provenance target: {resource}')
                        if 'id' in entry:
                            if not isinstance(entry['id'], str) or not entry['id'] or entry['id'] in ids:
                                raise ValueError('source ids must be non-empty and unique')
                            ids.add(entry['id'])
                    except ValueError as exc:
                        self.issue('error', path, str(exc))
            for target in self.links(path, body):
                incoming.add(target)
                if not target.exists():
                    self.issue('warning', path, f'ghost or broken link: {target.relative_to(self.root)}')
        for path, meta, _ in notes:
            if path.name not in ('index.md', 'log.md') and path not in incoming:
                self.issue('warning', path, 'orphan concept: no incoming Markdown links')
        return notes

    def coverage(self):
        coverage = {}
        for path, meta, _ in self.notes():
            if path.name in ('index.md', 'log.md') or not meta:
                continue
            entries = meta.get('sources', [])
            if not isinstance(entries, list):
                continue
            for entry in entries:
                try:
                    target = self.target(path, entry.get('resource')) if isinstance(entry, dict) else None
                    if target and target.is_relative_to(self.sources):
                        coverage.setdefault(target, []).append(str(path.relative_to(self.root)))
                except ValueError:
                    pass
        return coverage

    def scan(self):
        coverage = self.coverage()
        return [{'path': str(p.relative_to(self.root)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
                 'covered_by': sorted(coverage.get(p, [])), 'kind': 'guidance' if p.name in ('README.md', 'index.md') else 'source'}
                for p in self.files(self.sources)]

    def baseline(self):
        if not self.manifest.exists():
            raise ValueError('source manifest missing; run source-scan --update to establish an initial baseline')
        records = [json.loads(line) for line in self.manifest.read_text().splitlines() if line.strip()]
        result = {}
        for record in records:
            if not isinstance(record, dict) or not isinstance(record.get('path'), str) or not re.fullmatch(r'[0-9a-f]{64}', str(record.get('sha256', ''))):
                raise ValueError('invalid source manifest record')
            if record['path'] in result:
                raise ValueError('duplicate manifest path')
            result[record['path']] = record
        return result

    def delta(self, current, old):
        now = {r['path']: r for r in current}
        return {'added': sorted(now.keys() - old.keys()), 'removed': sorted(old.keys() - now.keys()),
                'changed': sorted(p for p in old.keys() & now.keys() if old[p]['sha256'] != now[p]['sha256'])}

    def build(self):
        notes = self.lint()
        if any(i['level'] == 'error' for i in self.issues):
            return
        records = []
        for path, meta, _ in notes:
            if path.name in ('index.md', 'log.md'):
                continue
            records.append({'path': str(path.relative_to(self.root)), 'type': meta['type'],
                            'title': meta.get('title', path.stem), 'description': meta.get('description', ''),
                            'tags': meta.get('tags', []), 'sources': meta.get('sources', [])})
        atomic(self.catalog, ''.join(json.dumps(r, default=str, ensure_ascii=False) + '\n' for r in records))
        print(f'Built {len(records)} catalog entries; curated indexes preserved.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--strict', action='store_true', help='fail on warnings too')
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('doctor', 'lint', 'build', 'source-lint', 'source-delta', 'source-coverage'):
        sub.add_parser(name)
    scan = sub.add_parser('source-scan')
    scan.add_argument('--update', action='store_true', help='write manifest; refuses changed/deleted source bytes')
    search = sub.add_parser('search-catalog')
    search.add_argument('--query', required=True)
    log = sub.add_parser('log')
    log.add_argument('--title', required=True)
    log.add_argument('--details', required=True)
    args = parser.parse_args()
    wiki = Wiki(args.root)
    try:
        if args.command == 'lint':
            wiki.lint()
        elif args.command == 'build':
            wiki.build()
        elif args.command == 'doctor':
            for name in ('AGENTS.md', 'SPEC.md', 'wiki/index.md', 'wiki/log.md'):
                if not (wiki.root / name).is_file():
                    wiki.issue('error', wiki.root / name, 'required framework file missing')
            print(json.dumps({'python': sys.version.split()[0], 'wiki_notes': len(wiki.files(wiki.bundle, '*.md')),
                              'source_files': len(wiki.files(wiki.sources)), 'catalog_exists': wiki.catalog.exists(),
                              'manifest_exists': wiki.manifest.exists()}, indent=2))
            if not wiki.catalog.exists() or not wiki.manifest.exists():
                wiki.issue('warning', wiki.root / 'scripts/wiki_tool.py', 'catalog or manifest not initialized')
        elif args.command.startswith('source-'):
            current = wiki.scan()
            if any(i['level'] == 'error' for i in wiki.issues):
                raise ValueError('invalid wiki metadata; refusing source report or manifest update')
            if args.command == 'source-coverage':
                print(json.dumps(current, indent=2))
            elif args.command == 'source-scan':
                if args.update:
                    if wiki.manifest.exists():
                        delta = wiki.delta(current, wiki.baseline())
                        if delta['changed'] or delta['removed']:
                            raise ValueError('refusing to replace baseline: changed or removed sources ' + json.dumps(delta))
                    atomic(wiki.manifest, ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in current))
                    print(f'Recorded {len(current)} source hashes and current coverage; source files untouched.')
                else:
                    print(json.dumps(current, indent=2))
            else:
                delta = wiki.delta(current, wiki.baseline())
                if args.command == 'source-delta':
                    print(json.dumps(delta, indent=2))
                for key in ('changed', 'removed'):
                    for path in delta[key]:
                        wiki.issue('error', wiki.root / path, f'immutable source {key} since baseline')
                for path in delta['added']:
                    wiki.issue('warning', wiki.root / path, 'new source not recorded in manifest')
                if args.command == 'source-lint':
                    for record in current:
                        if record['kind'] == 'source' and not record['covered_by']:
                            wiki.issue('warning', wiki.root / record['path'], 'source has no concept provenance coverage')
        elif args.command == 'search-catalog':
            if not wiki.catalog.exists():
                raise ValueError('catalog missing; run build first')
            for line in wiki.catalog.read_text().splitlines():
                record = json.loads(line)
                if args.query.casefold() in json.dumps(record, ensure_ascii=False).casefold():
                    print(json.dumps(record, ensure_ascii=False))
        elif args.command == 'log':
            if '\n' in args.title or '\n' in args.details or '\r' in args.title + args.details:
                raise ValueError('log title and details must be single-line')
            path = wiki.bundle / 'log.md'
            text = path.read_text(encoding='utf-8') if path.exists() else '# Wiki update log\n'
            date = dt.datetime.now(dt.timezone.utc).date().isoformat()
            entry = f'* **{args.title}**: {args.details}\n'
            heading = f'## {date}\n'
            if heading in text:
                text = text.replace(heading, heading + '\n' + entry, 1)
            else:
                match = re.search(r'^## ', text, re.M)
                position = match.start() if match else len(text)
                text = text[:position].rstrip() + '\n\n' + heading + '\n' + entry + '\n' + text[position:]
            atomic(path, text)
            print('Added UTC-dated log entry.')
        for issue in wiki.issues:
            print(f"{issue['level'].upper()}: {issue['path']}: {issue['message']}")
        if any(i['level'] == 'error' or args.strict for i in wiki.issues):
            return 1
        return 0
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2

if __name__ == '__main__':
    sys.exit(main())
