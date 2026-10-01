---
type: Synthesis
title: "Evaluation, security, production and learning references"
description: "Review of references 33–48 on evaluation, safety, deployment and learning."
tags: [source-derived, azure-ai-foundry, roadmap-references]
status: draft
stale_after: 2027-01-01T00:00:00Z
generated: { by: codex/gpt-6, at: 2026-10-01T20:00:00Z }
sources:
  - id: ref-33
    resource: ../sources/azure-ai-foundry/references/33-observability-in-generative-ai-microsoft-foundry.md
    title: "Observability in Generative AI - Microsoft Foundry"
  - id: ref-34
    resource: ../sources/azure-ai-foundry/references/34-azure-ai-evaluation-1-18-7-pypi.md
    title: "azure-ai-evaluation 1.18.7 - PyPI"
  - id: ref-35
    resource: ../sources/azure-ai-foundry/references/35-azure-ai-evaluation-package-microsoft-learn.md
    title: "azure.ai.evaluation package | Microsoft Learn"
  - id: ref-36
    resource: ../sources/azure-ai-foundry/references/36-scorers-and-llm-judges-azure-databricks-microsoft-learn.md
    title: "Scorers and LLM judges - Azure Databricks | Microsoft Learn"
  - id: ref-37
    resource: ../sources/azure-ai-foundry/references/37-azure-ai-evaluation-groundednessevaluator-class-microso.md
    title: "azure.ai.evaluation.GroundednessEvaluator class - Microsoft Learn"
  - id: ref-38
    resource: ../sources/azure-ai-foundry/references/38-with-the-red-team-sdk-can-we-test-only-safety-risks-or-.md
    title: "With the Red Team SDK, can we test only safety risks, or can we"
  - id: ref-39
    resource: ../sources/azure-ai-foundry/references/39-azure-ai-content-safety-prompt-shields-gu-free-guide-20.md
    title: "Azure AI Content Safety, Prompt Shields & Gu | Free Guide 2026"
  - id: ref-40
    resource: ../sources/azure-ai-foundry/references/40-enhance-ai-security-with-azure-prompt-shields-and-azure.md
    title: "Enhance AI security with Azure Prompt Shields and Azure AI"
  - id: ref-41
    resource: ../sources/azure-ai-foundry/references/41-from-agent-deployed-to-agent-ready-agent-acceptance-gat.md
    title: "From \"Agent Deployed\" to \"Agent Ready\" - Agent Acceptance Gateway"
  - id: ref-42
    resource: ../sources/azure-ai-foundry/references/42-build-ai-applications-with-pre-made-templates-azure-doc.md
    title: "Build AI applications with pre-made templates - Azure documentation"
  - id: ref-43
    resource: ../sources/azure-ai-foundry/references/43-azure-ai-certification-microsoft-q-a.md
    title: "Azure AI Certification - Microsoft Q&A"
  - id: ref-44
    resource: ../sources/azure-ai-foundry/references/44-study-guide-for-exam-ai-900-microsoft-azure-ai-fundamen.md
    title: "Study guide for Exam AI-900: Microsoft Azure AI Fundamentals"
  - id: ref-45
    resource: ../sources/azure-ai-foundry/references/45-ai-3016-develop-generative-ai-apps-in-azure-ai-foundry-.md
    title: "AI-3016: Develop Generative AI Apps in Azure AI Foundry - CloudThat"
  - id: ref-46
    resource: ../sources/azure-ai-foundry/references/46-course-ai-3026-a-develop-ai-agents-on-azure-microsoft-l.md
    title: "Course AI-3026-A: Develop AI agents on Azure - Microsoft Learn"
  - id: ref-47
    resource: ../sources/azure-ai-foundry/references/47-learn-microsoft.md
    title: "Learn - Microsoft"
  - id: ref-48
    resource: ../sources/azure-ai-foundry/references/48-study-guide-for-exam-ai-102-designing-and-implementing-.md
    title: "Study guide for Exam AI-102: Designing and Implementing a"
---

# Evidence review

Microsoft Observability [33](../sources/azure-ai-foundry/references/33-observability-in-generative-ai-microsoft-foundry.md) covers evaluation, monitoring and tracing. Azure AI Evaluation [34–35] and GroundednessEvaluator [37] are SDK/API sources; Databricks [36] is adjacent. Scores are measurements, not proof: groundedness checks claims against supplied context. Q&A [38](../sources/azure-ai-foundry/references/38-with-the-red-team-sdk-can-we-test-only-safety-risks-or-.md) has conflicting human and AI-generated answers; accepted moderator answer says Red Team is not full OWASP Top 10 coverage. OpenExamPrep [39] is secondary; official blog #40 was not text-readable. Gateway #41 and templates #42 were inaccessible/JS-only. AI-900 guide [44](../sources/azure-ai-foundry/references/44-study-guide-for-exam-ai-900-microsoft-azure-ai-fundamen.md) says exam retired June 30, 2026; Q&A #43 conflicts. Verify credentials status. AI-3026 #46 is Microsoft training; CloudThat #45 is marketing. Confirm AI-102 status.

## Review

Evaluator/package/credential details change. Pin versions and prefer current primary docs. See [RAG, SDKs, agents and MCP](rag-agents-and-mcp.md).
