---
type: Reference
title: Open Knowledge Format v0.2
description: The local format contract for portable, human-readable, agent-friendly knowledge bundles.
tags: [reference]
status: stable
generated:
  by: codex/gpt-6
  at: 2026-10-01T17:18:00Z
sources:
  - id: local-spec
    resource: ../SPEC.md
    title: Open Knowledge Format specification
---

# Bundle contract

This bundle follows [the local OKF v0.2 specification](../SPEC.md). A bundle is a directory tree of Markdown files. Each non-reserved concept document has YAML frontmatter and a non-empty `type`; `index.md` provides progressive disclosure and `log.md` records updates.

# Core conventions

Concepts use relative Markdown links to express relationships. This bundle follows the distinction that tags answer **what is this?**, while links and topic pages answer **what is this about?**. `type` is the primary classification; `tags` are limited to lightweight metadata and broad facets. A link may intentionally point to a not-yet-written concept, creating a ghost link that can become live later. `index.md` files act as curated Maps of Content for progressive disclosure.

Provenance belongs in the `sources` frontmatter field. Generated and verification actors use the forms `codex/<version>`, `human:<id>`, or `process:<id>`. Optional trust, lifecycle, and attested-computation fields are used only when their evidence and contracts exist.

# This bundle

The bundle root is [`wiki/`](index.md), and it declares `okf_version: "0.2"` in its root index. The repository-level [maintenance schema](../AGENTS.md) explains how an agent should produce and consume these documents.
