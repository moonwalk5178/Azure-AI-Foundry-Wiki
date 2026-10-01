import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

TOOL = Path(__file__).resolve().parents[1] / 'scripts/wiki_tool.py'
spec = importlib.util.spec_from_file_location('wiki_tool', TOOL)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ToolTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'wiki').mkdir()
        (self.root / 'sources').mkdir()
        (self.root / 'sources/raw.md').write_text('immutable original')
        (self.root / 'wiki/index.md').write_text('---\nokf_version: "0.2"\n---\n# Topics\n* [A](a.md) - curated text\n')
        (self.root / 'wiki/log.md').write_text('# History\n\n## 2026-01-01\n* Initial\n')
        self.note = self.root / 'wiki/a.md'
        self.note.write_text('---\ntype: Custom Type\ntitle: A\ngenerated: {by: process:test, at: 2026-01-01T00:00:00Z}\nsources:\n  - resource: ../sources/raw.md\n---\n# A\n[Future](future.md)\n')

    def run_tool(self, *args):
        return subprocess.run([sys.executable, str(TOOL), '--root', str(self.root), *args], capture_output=True, text=True)

    def test_build_preserves_sources_and_curated_index(self):
        source = (self.root / 'sources/raw.md').read_bytes()
        index = (self.root / 'wiki/index.md').read_bytes()
        self.assertEqual(self.run_tool('build').returncode, 0)
        self.assertEqual(source, (self.root / 'sources/raw.md').read_bytes())
        self.assertEqual(index, (self.root / 'wiki/index.md').read_bytes())
        self.assertIn('Custom Type', (self.root / 'wiki/catalog.jsonl').read_text())

    def test_ghost_warning_and_strict_failure(self):
        self.assertEqual(self.run_tool('lint').returncode, 0)
        self.assertEqual(self.run_tool('--strict', 'lint').returncode, 1)

    def test_missing_provenance_is_error(self):
        self.note.write_text(self.note.read_text().replace('../sources/raw.md', '../sources/missing.md'))
        self.assertEqual(self.run_tool('lint').returncode, 1)
        self.assertEqual(self.run_tool('build').returncode, 1)
        self.assertFalse((self.root / 'wiki/catalog.jsonl').exists())

    def test_source_change_cannot_be_blessed(self):
        self.assertEqual(self.run_tool('source-scan', '--update').returncode, 0)
        baseline = (self.root / 'maintenance/source-manifest.jsonl').read_bytes()
        (self.root / 'sources/raw.md').write_text('changed')
        self.assertEqual(self.run_tool('source-lint').returncode, 1)
        self.assertEqual(self.run_tool('source-scan', '--update').returncode, 2)
        self.assertEqual(baseline, (self.root / 'maintenance/source-manifest.jsonl').read_bytes())

    def test_new_sources_coverage_and_removal(self):
        self.run_tool('source-scan', '--update')
        (self.root / 'sources/new.md').write_text('new')
        result = self.run_tool('source-delta')
        self.assertIn('new.md', result.stdout)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(self.run_tool('source-scan', '--update').returncode, 0)
        self.assertIn('raw.md', self.run_tool('source-coverage').stdout)
        (self.root / 'sources/new.md').unlink()
        self.assertEqual(self.run_tool('source-lint').returncode, 1)

    def test_invalid_yaml_duplicate_keys(self):
        self.note.write_text('---\ntype: Concept\ntype: Reference\n---\n')
        self.assertEqual(self.run_tool('lint').returncode, 1)
        self.assertEqual(self.run_tool('source-scan', '--update').returncode, 2)

    def test_bundle_absolute_paths_and_code_examples(self):
        self.note.write_text(self.note.read_text() + '\n[A](/a.md)\n```markdown\n[Example](../../outside.md)\n```\n')
        result = self.run_tool('lint')
        self.assertEqual(result.returncode, 0)
        self.assertNotIn('outside', result.stdout)

    def test_path_escape_rejected(self):
        self.note.write_text(self.note.read_text().replace('../sources/raw.md', '../../outside.md'))
        self.assertEqual(self.run_tool('lint').returncode, 1)

    def test_log_is_dated_and_keeps_history(self):
        self.assertEqual(self.run_tool('log', '--title', 'Lint', '--details', 'Checked structure.').returncode, 0)
        text = (self.root / 'wiki/log.md').read_text()
        self.assertIn('## 2026-01-01', text)
        self.assertIn('Checked structure.', text)
        self.assertEqual(self.run_tool('lint').returncode, 0)

    def test_search(self):
        self.run_tool('build')
        self.assertIn('wiki/a.md', self.run_tool('search-catalog', '--query', 'custom type').stdout)

if __name__ == '__main__':
    unittest.main()
