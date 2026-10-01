---
type: Synthesis
title: "RAG, SDKs, agents and MCP integrations"
description: "Review of references 15–32 on retrieval, SDKs, agents and MCP."
tags: [source-derived, azure-ai-foundry, roadmap-references]
status: draft
stale_after: 2027-01-01T00:00:00Z
generated: { by: codex/gpt-6, at: 2026-10-01T20:00:00Z }
sources:
  - id: ref-15
    resource: ../sources/azure-ai-foundry/references/15-fine-tuning-vs-rag-key-differences-explained-2026-guide.md
    title: "Fine-Tuning vs RAG: Key Differences Explained (2026 Guide) - Orq.ai"
  - id: ref-16
    resource: ../sources/azure-ai-foundry/references/16-what-is-rag-the-architecture-deep-dive-on-azure-ai-foun.md
    title: "What is RAG? The Architecture Deep Dive on Azure AI Foundry"
  - id: ref-17
    resource: ../sources/azure-ai-foundry/references/17-ai-app-architecture-for-startups-microsoft-learn.md
    title: "AI App Architecture for Startups | Microsoft Learn"
  - id: ref-18
    resource: ../sources/azure-ai-foundry/references/18-how-to-develop-ai-apps-and-agents-in-azure-a-visual-gui.md
    title: "How to develop AI Apps and Agents in Azure - A Visual Guide"
  - id: ref-19
    resource: ../sources/azure-ai-foundry/references/19-how-to-get-started-with-ai-agent-development-on-azure-s.md
    title: "How to Get Started with AI Agent Development on Azure? - SoluLab"
  - id: ref-20
    resource: ../sources/azure-ai-foundry/references/20-azure-ai-projects-client-library-for-python-microsoft-l.md
    title: "Azure AI Projects client library for Python | Microsoft Learn"
  - id: ref-21
    resource: ../sources/azure-ai-foundry/references/21-azure-ai-agents-client-library-for-python-microsoft-lea.md
    title: "Azure AI Agents client library for Python | Microsoft Learn"
  - id: ref-22
    resource: ../sources/azure-ai-foundry/references/22-use-code-interpreter-with-microsoft-foundry-agents.md
    title: "Use Code Interpreter with Microsoft Foundry agents"
  - id: ref-23
    resource: ../sources/azure-ai-foundry/references/23-from-zero-to-microsoft-foundry-creating-agents-via-ai-p.md
    title: "From Zero to Microsoft Foundry: Creating Agents Via AI Projects"
  - id: ref-24
    resource: ../sources/azure-ai-foundry/references/24-azure-ai-projects-client-library-for-python-microsoft-l.md
    title: "Azure AI Projects client library for Python | Microsoft Learn"
  - id: ref-25
    resource: ../sources/azure-ai-foundry/references/25-smart-ai-integration-with-the-model-context-protocol-mc.md
    title: "Smart AI integration with the Model Context Protocol (MCP) ... part 1"
  - id: ref-26
    resource: ../sources/azure-ai-foundry/references/26-deploying-ai-agents-at-scale-valentina-alto-medium.md
    title: "Deploying AI Agents at scale - Valentina Alto - Medium"
  - id: ref-27
    resource: ../sources/azure-ai-foundry/references/27-introducing-model-context-protocol-mcp-in-azure-ai-foun.md
    title: "Introducing Model Context Protocol (MCP) in Azure AI Foundry"
  - id: ref-28
    resource: ../sources/azure-ai-foundry/references/28-model-context-protocol-mcp-integrating-azure-openai-for.md
    title: "Model Context Protocol (MCP): Integrating Azure OpenAI for"
  - id: ref-29
    resource: ../sources/azure-ai-foundry/references/29-announcing-model-context-protocol-support-preview-in-az.md
    title: "Announcing Model Context Protocol Support (preview) in Azure AI"
  - id: ref-30
    resource: ../sources/azure-ai-foundry/references/30-getting-started-with-ai-foundry-and-the-snowflake-manag.md
    title: "Getting Started with AI Foundry and the Snowflake Managed MCP"
  - id: ref-31
    resource: ../sources/azure-ai-foundry/references/31-quickstart-azure-ai-foundry-sql-mcp-server-microsoft-le.md
    title: "Quickstart - Azure AI Foundry - SQL MCP Server | Microsoft Learn"
  - id: ref-32
    resource: ../sources/azure-ai-foundry/references/32-building-smarter-ai-agents-with-azure-ai-foundry-and-mo.md
    title: "Building Smarter AI Agents with Azure AI Foundry and Model"
---

# Evidence review

RAG/fine-tuning pieces [15–16] are secondary. Microsoft architecture [17](../sources/azure-ai-foundry/references/17-ai-app-architecture-for-startups-microsoft-learn.md) stresses measuring end-to-end latency, trimming prompt/retrieval work, traffic shaping, simplifying orchestration and bounded retries. Primary SDK refs include Agents [21](../sources/azure-ai-foundry/references/21-azure-ai-agents-client-library-for-python-microsoft-lea.md) and Projects [20](../sources/azure-ai-foundry/references/20-azure-ai-projects-client-library-for-python-microsoft-l.md), [24](../sources/azure-ai-foundry/references/24-azure-ai-projects-client-library-for-python-microsoft-l.md); note locale/preview differences. MCP material spans preview announcement [29](../sources/azure-ai-foundry/references/29-announcing-model-context-protocol-support-preview-in-az.md), Snowflake [30], SQL MCP [31], and tutorials [25], [27–28], [32]. Some could not be read; notes identify access limits.

## Review

Verify current transport, authentication, allowed tools, approval behavior and server authorization before implementing MCP. Preview guidance changes quickly. See [platform and costs](platform-and-costs.md) and [evaluation/security](evaluation-security-and-learning.md).
