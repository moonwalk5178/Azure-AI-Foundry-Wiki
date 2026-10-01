# Azure AI Foundry Wiki maintenance schema

This repository is an LLM-maintained knowledge base about Azure AI Foundry. Follow these rules for every session.

## Layout

- `sources/` contains curated raw source material. Treat it as immutable: never rewrite, summarize in place, or delete source files.
- `wiki/` is the Open Knowledge Format (OKF) v0.2 knowledge bundle. Generated and maintained concepts live here.
- `llm-wiki.md` explains the idea; `SPEC.md` is the local OKF v0.2 specification.

## Source-of-truth and provenance

The raw material in `sources/` is the source of truth. Wiki concepts are derived knowledge and must not present an unsupported claim as fact.

Every concept created or materially revised should use OKF frontmatter with:

- a non-empty `type`;
- `title`, `description`, and useful `tags` when applicable;
- `sources` entries pointing to the material used;
- `generated: { by: codex/<version>, at: <UTC timestamp> }`;
- `verified` only when a human or deterministic process has actually verified the content;
- `status` and `stale_after` when freshness matters.

### Tags, topics, and links

Use the Wanderloots distinction adopted by this wiki:

- **What is this?** Use `type` first (`Concept`, `Synthesis`, `Playbook`, `Reference`, `Template`) and use `tags` only for lightweight classification or note metadata such as `source-derived`, `person`, `book`, or `topic-hub`.
- **What is this about?** Use standard Markdown links in the body to point to concepts, people, places, and source records. A link may point to a not-yet-written concept; intentional ghost links are allowed.
- Do not use topical tags as a substitute for the relationship graph. If a topic deserves to be discoverable and connected, make it a link and create its page when evidence or inbound links justify it.
- `index.md` files are curated Maps of Content: they are navigation hubs, not replacements for concept links.

The `tags` field remains valid OKF and may contain broad facets when useful, but the wiki's primary subject structure is its link graph.

Use actor names in the form `codex/<version>`, `human:<id>`, or `process:<id>`. Do not invent human verification.

## Workflows

### Ingest

1. Inspect the new or changed files in `sources/` without editing them.
2. Identify the relevant existing concepts through `wiki/index.md` and directory indexes.
3. Create or update the smallest useful set of concepts. Preserve existing claims unless the source supports a correction.
4. Record provenance in frontmatter and cite sources in the body where useful.
5. Update affected indexes and append a newest-first entry to `wiki/log.md`.
6. Report uncertainty, contradictions, and claims that need human review.

### Query

Start with `wiki/index.md`, follow relevant links, and answer from the wiki plus cited source material. Distinguish sourced facts, synthesis, and open questions. File durable, user-requested answers as new concepts.

### Lint

Run `python3 scripts/wiki_tool.py lint`, `python3 scripts/wiki_tool.py build`, and `python3 scripts/wiki_tool.py source-lint` before finishing meaningful wiki changes. After adding sources, use `source-scan --update` to record new hashes and refresh coverage; do not overwrite a baseline that reports changed or removed sources. See [tool commands](scripts/README.md). These structural checks supplement the semantic review below; they do not verify claims or replace curated Maps of Content.

Check OKF conformance, broken or missing links, orphan concepts, stale claims, missing provenance, contradictions, and index/log freshness. Make only evidence-backed repairs and log the pass.

## OKF rules

- The `wiki/` directory is the bundle root and targets `okf_version: "0.2"`.
- Every non-reserved `.md` file under `wiki/` must begin with parseable YAML frontmatter containing a non-empty `type`.
- `index.md` and `log.md` are reserved and must follow OKF structure.
- Use standard relative Markdown links for relationships between concepts.
- Consumers must tolerate unknown types, broken links, and optional fields; do not add bespoke required fields to existing concepts without documenting the change.
- Do not create an Attested Computation unless there is an actual sanctioned computation, executor, and deterministic attester.

## Safe editing

Prefer focused edits. Preserve user changes. Never modify `sources/` during normal wiki maintenance. Before finishing, inspect the diff and run a lightweight structural check over `wiki/`.

