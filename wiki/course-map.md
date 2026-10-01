---
type: Map
title: "Microsoft Foundry course map"
description: "Learner-facing route through a 20-week Microsoft Foundry study plan, with the first lesson ready."
tags: [learning, map, azure-ai-foundry]
status: draft
generated:
  by: codex/gpt-6
  at: 2026-10-01T20:00:00Z
sources:
  - id: roadmap
    resource: ../sources/azure-ai-foundry/Azure AI Foundry Learning Roadmap.docx
    title: Original learning roadmap
  - id: phase-1-plan
    resource: ../sources/inbox/azure-foundry-phase-1-lesson-plan.md
    title: Phase 1 lesson plan
---

# Start learning

Work through the course in order, keeping your diagrams, decisions, and questions as your study notes. This 20-week sequence adapts the roadmap and Phase 1 lesson plan. **Only Week 1 has a complete lesson today; later topics are planned, not finished instructional material.**

**Start here:** [Week 1: Understand the Foundry platform and access model](lessons/week-01-foundry-platform-and-access.md)

| Phase | Weeks | Focus | Milestone |
|---|---:|---|---|
| 1. Platform architecture and economics | 1–4 | Platform boundaries, identity/RBAC, networking, deployment choices, quotas and cost controls | Resource/identity diagram, network decision record, model comparison, cost estimate |
| 2. Generative patterns | 5–8 | RAG versus fine-tuning, retrieval quality, SDKs, application patterns | Grounded application design and retrieval evaluation |
| 3. Agents and MCP | 9–12 | Agent basics, tools, hosted versus prompt agents, MCP, orchestration | Tool-using agent design with explicit access boundaries |
| 4. Evaluation and trustworthy AI | 13–16 | Evaluation datasets, metrics, tracing, monitoring, safety testing | Evaluation and safety test plan |
| 5. Production deployment | 17–20 | Deployment options, identity, private networking, acceptance, operations | Production readiness review and capstone |

## Phase 1 sequence

1. **Week 1 — Platform and access model:** [lesson](lessons/week-01-foundry-platform-and-access.md). Draw the resource/project and identity map; explain control plane versus data plane.
2. **Week 2 — Network and data boundaries:** planned. Trace requests, private access, dependencies, and data movement.
3. **Week 3 — Models and deployment choices:** planned. Compare model fit, deployment modes, quotas, and regional availability.
4. **Week 4 — Cost and operating guardrails:** planned. Build low/expected/high usage assumptions and separate alerts from hard limits.

## How to study

1. Read a lesson and its linked primary sources.
2. Make the diagram or decision artifact.
3. Explain the checkpoint without looking at the page.
4. Mark environment-specific details for verification.
5. Bring your artifact or questions back to the wiki so later lessons can build on them.

Provisioning Azure resources is optional. Before creating anything, confirm subscription permissions, region/model availability, organizational policy, quota, and expected charges.

The roadmap is a teaching path, not a certification syllabus. Its older Hub/Project references are historical planning material. Week 1 was checked against current Microsoft Learn guidance; product behavior and roles can change. See the [proposed roadmap](learning-roadmap.md) for its original outline and caveats.
