---
type: Playbook
title: Azure AI Foundry Wiki operating playbook
description: Repeatable workflows for ingesting sources, querying knowledge, and maintaining the OKF bundle.
tags: [playbook]
status: active
generated:
  by: codex/gpt-6
  at: 2026-10-01T17:18:00Z
sources:
  - id: local-spec
    resource: ../SPEC.md
    title: Open Knowledge Format v0.2 specification
---

# Ingest

Inspect new or changed files in [sources/](../sources/README.md) without editing them. Start from the [bundle index](index.md), find relevant existing concepts, and create or revise only the smallest useful set supported by the source. Record provenance in frontmatter and cite material in the body where useful. Update affected Maps of Content and append a dated entry to [log.md](log.md). Run `python3 scripts/wiki_tool.py source-scan --update` only after reviewing reported changes; it refuses to silently baseline modified or removed source files.

# Query

Start with the bundle index, follow concept links, and consult cited source material when the wiki is incomplete or disputed. Distinguish sourced facts, synthesis, inference, and open questions. File durable answers as concepts when requested.

# Lint and maintenance

Run:

```sh
python3 scripts/wiki_tool.py doctor
python3 scripts/wiki_tool.py lint
python3 scripts/wiki_tool.py build
python3 scripts/wiki_tool.py source-lint
python3 -m unittest discover -s tests -v
```

The tool checks structure, provenance paths, links, source hashes, and coverage. It does not judge factual accuracy, semantic contradictions, or completeness of Maps of Content; review those directly. Read [the tool guide](../scripts/README.md) for details.

# Boundaries

Never rewrite or delete raw sources during routine wiki maintenance. Do not claim human verification without an explicit review. Create an Attested Computation only when a sanctioned computation, executor, and deterministic attester exist.
