# Wiki maintenance tool

Run with Python 3.10 or newer. Install the YAML parser once:

```sh
python3 -m pip install -r scripts/requirements.txt
```

Run from any working directory; the repository root defaults to the script's parent directory. Use `--root /path/to/repository` before the command to target another checkout.

| Command | Behavior |
| --- | --- |
| `doctor` | Check framework files, Python version, note counts, and generated artifact availability. |
| `lint` | Check OKF YAML, type, tags, actors/timestamps, provenance targets, reserved files, ghost links, orphan concepts, and stale dates. |
| `build` | Lint, then atomically rebuild `wiki/catalog.jsonl`. Preserve curated indexes and Maps of Content. |
| `source-scan` | Report SHA-256 hashes and concept provenance coverage for source files. |
| `source-scan --update` | Establish the initial manifest or add new sources/refresh coverage. Refuse changed or removed source bytes. |
| `source-lint` | Compare source hashes with the manifest and report sources without concept provenance coverage. |
| `source-delta` | Report sources added, removed, or changed since the manifest baseline. |
| `source-coverage` | Show which concepts cite each source. |
| `search-catalog --query "text"` | Search catalog records case-insensitively. Run build after wiki changes to refresh it. |
| `log --title "Lint" --details "Checked structure."` | Add an explicit UTC-dated log entry, newest first. |

Example maintenance pass:

```sh
python3 scripts/wiki_tool.py doctor
python3 scripts/wiki_tool.py lint
python3 scripts/wiki_tool.py build
python3 scripts/wiki_tool.py source-lint
```

After adding sources and ingesting them, run `source-scan --update` to record new files and refresh coverage. The manifest is `maintenance/source-manifest.jsonl`. It contains hashes and current coverage, not copies of sources. README and index files under `sources/` are guidance and do not need derived concept coverage, but their bytes are tracked too.

Exit codes: 0 means no errors; 1 means checks found errors; 2 means an operational failure. Warnings do not fail by default. Put `--strict` before the command to fail on warnings too. Unknown OKF types and fields are supported. Missing concept links are warnings because intentional ghost links are permitted. Missing explicit local provenance files are errors. External URLs and prose scope descriptors are not fetched or verified.

No command edits, moves, or deletes sources. A hash baseline detects changes only after initialization; it cannot attest to earlier source history. Existing legitimate source moves or corrections need explicit human review of the manifest change; the tool does not silently accept them. The tool never sets `verified` metadata.

This is structural lint, not a factual or semantic judge. Agents must still inspect contradictions, unsupported claims, meaningful topic links, intentional ghost links, index completeness, and freshness. Markdown link extraction supports common inline and reference forms; complex Markdown constructs and URL fragments require review. Catalog search covers metadata, not full-text source search.

When bootstrapping a new wiki, copy the script, dependencies, tests, and this guidance. Do not copy the exemplar's catalog or source manifest: run `build` and `source-scan --update` against the clean new baseline to generate its own artifacts. Do not import the exemplar's accumulated source coverage or hashes.

Run regression tests:

```sh
python3 -m unittest discover -s tests -v
```
