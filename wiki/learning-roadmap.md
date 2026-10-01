---
type: Reference
title: "Azure AI Foundry learning roadmap"
description: "A five-phase, 20-week learning sequence and retail-agent capstone proposed by the uploaded roadmap."
tags: [source-derived, learning-roadmap]
status: draft
stale_after: 2026-12-31T23:59:59Z
generated:
  by: codex/gpt-6
  at: 2026-10-01T18:59:49Z
sources:
  - id: roadmap-docx
    resource: ../sources/azure-ai-foundry/Azure AI Foundry Learning Roadmap.docx
    title: Original learning roadmap
  - id: roadmap-html
    resource: ../sources/azure-ai-foundry/azure_ai_foundry_roadmap.html
    title: Interactive roadmap companion
  - id: roadmap-references
    resource: ../sources/azure-ai-foundry/roadmap-references.md
    title: Roadmap citation register
  - id: phase-1-lesson-plan
    resource: ../sources/inbox/azure-foundry-phase-1-lesson-plan.md
    title: Microsoft Foundry Phase 1 lesson plan
  - id: phase-1-source-register
    resource: ../sources/inbox/azure-foundry-phase-1-source-register.md
    title: Microsoft Foundry Phase 1 source register
---

# Purpose and scope

This page captures the learning sequence and project proposal in the DOCX and its interactive HTML companion. It records their recommendations as proposals, not verified Azure architecture guidance. The raw [DOCX](../sources/azure-ai-foundry/Azure%20AI%20Foundry%20Learning%20Roadmap.docx) and [HTML companion](../sources/azure-ai-foundry/azure_ai_foundry_roadmap.html) remain the evidence; the [48-entry citation register](../sources/azure-ai-foundry/roadmap-references.md) preserves the original numbered bibliography.

# Proposed five-phase sequence

## Phase 1: platform architecture and economics (weeks 1–4)

Study the Hub/Project hierarchy, governance and access control, network isolation, model selection, deployment types, and cost controls. Compare Pay-As-You-Go (PAYG), Provisioned Throughput Units (PTUs), and managed compute; account for token limits, budget alerts, and supporting services.

The sources give specific claims, including model-catalog size, a 50–80% inference-cost share, and a 150–200 million tokens/month PTU break-even range. Treat these figures as unverified and time-sensitive. Confirm current model availability, pricing, network behavior, and access roles before use. The DOCX points chiefly to bibliography entries 1–14.

The companion [Phase 1 lesson plan](../sources/inbox/azure-foundry-phase-1-lesson-plan.md) narrows this phase to four weeks and five deliverables: a control-plane/data-plane and resource/project diagram, a least-privilege identity and RBAC matrix, a network decision record, a model and deployment comparison, and a low/expected/high cost estimate with guardrails. It explicitly separates sourced facts, calculations, design choices, and open questions. Its [source register](../sources/inbox/azure-foundry-phase-1-source-register.md) prioritizes current Microsoft Learn material for platform boundaries, networking, model deployment, provisioned throughput, budgets, and alerts.

The lesson plan is a study guide, not verified architecture guidance. Its network, role, model, region, pricing, quota, and product-availability claims require validation in the target subscription and region. In particular, budgets and cost alerts are described as notification and accountability controls, not automatic spending cutoffs; preventative controls must be designed separately.

## Phase 2: generative patterns and orchestration (weeks 5–8)

Compare retrieval-augmented generation (RAG), fine-tuning, and hybrid patterns; study retrieval quality and freshness; explore Prompt Flow; and practice with Azure AI Projects and Agents SDKs. The HTML adds a RAG-versus-fine-tuning decision aid and illustrative vector-store code.

The source's statement that RAG prevents hallucinations is too strong: retrieval can provide evidence but does not guarantee a correct answer. Verify SDK examples, APIs, and service behavior against current package documentation. The DOCX points chiefly to entries 15–24.

## Phase 3: agents and the Model Context Protocol (weeks 9–12)

Compare managed prompt agents with hosted agents, learn tool calling, explore code-execution tools, and build an MCP integration. The HTML includes sample MCP and multi-agent routing snippets.

The roadmap describes schema discovery and agent access to SQL or other external systems. Those are proposals, not guarantees. Verify current Foundry support, authentication, transport, authorization, and security boundaries before implementation. The DOCX points chiefly to entries 19–32.

## Phase 4: evaluation and trustworthy AI (weeks 13–16)

Study evaluation datasets and metrics, red-team testing, observability, tracing, and content-safety controls. The HTML adds an evaluation-metrics visualization and self-assessment quiz.

Metric definitions, score ranges, evaluator names, and product references require current documentation checks. Scores do not prove safety or correctness; evaluation design depends on the application. The DOCX points chiefly to entries 33–41.

## Phase 5: production deployment and enterprise scalability (weeks 17–20)

Compare App Service, Container Apps, and AKS; study containerization, API Management, deployment acceptance, and production observability. Connect deployment choices to earlier work on cost, identity, networking, and evaluation. The DOCX points chiefly to entries 17–19 and 41–42.

# Capstone proposal: Intelligent Enterprise Retail Agent

The roadmap proposes a practice system that answers HR-policy questions from synthetic documents and retrieves mock retail inventory and pricing from SQL through an MCP server. Its workflow is to set up a governed Foundry workspace; ground policy answers in synthetic documents; expose mock inventory through a test MCP server; route questions to retrieval or database tools; evaluate answers and tool arguments; test prompt-injection defenses; then deploy and trace the application.

This is a learning-project outline, not a validated production design. Check the named models, services, roles, SDK objects, evaluators, and deployment features against current documentation and the target environment. Use synthetic data and explicit least-privilege controls.

# Interactive study aids and continued learning

The HTML adds a progress tracker, PAYG/PTU cost simulator, RAG/fine-tuning selector, metrics chart, capstone-flow visualization, and certification quiz. These illustrate the page's assumptions; they are not authoritative calculators or validation results. Embedded Python snippets were not executed.

The sources list AI-900, AI-3016, AI-3026, and AI-102 as milestones. Certification names, exam objectives, and availability change; verify the current Microsoft credentials catalog before planning around them.

# Review status

The 48 bibliography entries are titles and links only. They have not been reviewed here, so the roadmap's claims and citations remain unverified. Pricing, model inventory, product names, APIs, previews, and certifications should be rechecked before use.
