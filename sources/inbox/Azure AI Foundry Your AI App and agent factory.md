---
title: "Azure AI Foundry: Your AI App and agent factory"
type: "source"
source_type: "web"
tags:
  - "inbox"
topics:
  - "[[Artificial Intelligence Platforms]]"
  - "[[AI Agents]]"
  - "[[Multi-Agent Orchestration]]"
  - "[[Responsible AI]]"
  - "[[Enterprise Technology]]"
reference: "https://azure.microsoft.com/en-us/blog/azure-ai-foundry-your-ai-app-and-agent-factory/"
created: 2026-10-01
review: 2027-10-01
---
# Azure AI Foundry: Your AI App and agent factory

---

## Summary

>[!info]
>Date: 2025-05-19T16:00:00+00:00
> Author: [[Asha Sharma]]
> Description: Today, we’re announcing the next evolution in this journey with Azure AI Foundry—an industrial-grade AI Factory where ideas become production-ready agents in hours! Learn more.

## Overview
The page is a Microsoft Azure Blog announcement describing ten innovations in Azure AI Foundry, presented at Microsoft Build 2025. It frames Foundry as an end-to-end platform for building, deploying, monitoring, securing, and managing AI applications and agents across cloud, on-premises, and edge environments.

## Key Points
1. **Expanded model catalog:** The article announces access or planned access to models including Grok 3, Flux Pro 1.1, Sora, and more than 10,000 open-source Hugging Face models. It also highlights fine-tuning options, including LoRA, QLoRA, DPO, and a developer tier without hosting fees.
2. **Model selection and capacity:** A model router is intended to select an appropriate Azure OpenAI model for a prompt. Reserved capacity is being extended to Azure OpenAI and selected Foundry models, with access through a unified API and MCP server.
3. **Managed agent development:** Azure AI Foundry Agent Service is described as generally available. It provides managed infrastructure, orchestration, templates, actions, enterprise-data connectors, and deployment options for Microsoft 365, Slack, and Twilio.
4. **Multi-agent orchestration:** Agents can work together as connected agents. Stateful workflows support context, error handling, and long-running processes. The article emphasizes A2A communication and MCP as interoperability standards across multiple clouds and on-premises environments.
5. **Agentic retrieval:** Azure AI Search’s agentic retrieval uses conversation context and an embedded language model to decompose complex queries, search in parallel, and produce cited answers. The article reports early-test relevance improvements of up to approximately 40% for complex questions, but does not provide detailed methodology.
6. **Observability:** Foundry Observability is presented as a preview capability offering metrics, traces, diagnostics, evaluation benchmarks, CI/CD integrations, and Azure Monitor integration.
7. **Agent identity and governance:** Microsoft Entra Agent ID assigns agents distinct identities in an organization’s directory, enabling access control and future support for policies such as Conditional Access, multifactor authentication, and least-privilege roles.
8. **Trust and security:** The platform includes agent evaluators, an AI Red Teaming Agent, Prompt Shields with “Spotlighting,” guardrails, Defender for Cloud integration, and governance integrations with Credo AI, Saidot, and Microsoft Purview.
9. **Local and edge execution:** Foundry Local is described as a Windows and Mac runtime for offline or local AI applications. Azure Arc integration is planned for centralized management of on-device deployments.
10. **Research and future capabilities:** Foundry Labs projects include Project Amelie for automated machine-learning pipelines, Magentic-UI for web tasks, TypeAgent for long-term memory, and biology-focused systems such as EvoDiff and BioEmu.

## Important Concepts
- **AI agent:** A software system that can use models, tools, data, and workflows to perform tasks.
- **Agentic retrieval:** Retrieval that uses an AI system to interpret, decompose, and search complex queries before generating a grounded response.
- **Multi-agent orchestration:** Coordination of specialized agents to complete a larger workflow.
- **MCP:** The Model Context Protocol, described here as a way for models or agents to share and interpret contextual data consistently.
- **A2A communication:** Agent-to-Agent communication for exchanging information and coordinating tasks.
- **Observability:** Monitoring and tracing of agent behavior, performance, tool calls, quality, and operational metrics.

## Examples and Applications
The article cites enterprise process automation, financial approvals, supply-chain operations, healthcare tumor-board workflows, enterprise search, manufacturing with unreliable connectivity, remote field service, and automated machine-learning pipeline creation. It names Heineken, Carvana, Fujitsu, and Stanford Medicine as examples of organizations or scenarios associated with the platform.

## Interpretation
The central strategic theme is that AI development is moving from isolated model experimentation toward managed, production-oriented systems. The article positions Azure AI Foundry as a platform connecting models, agents, enterprise data, software development, security, governance, and deployment locations.

## Limitations and Open Questions
- Several capabilities are announced as preview, planned, experimental, or coming soon rather than generally available.
- The article does not provide detailed pricing, service limits, regional availability, performance benchmarks, or comparative evaluations.
- The approximately 40% retrieval improvement is attributed to early tests, but the test design and baseline are not described.
- Claims about security, governance, and interoperability describe intended capabilities; operational effectiveness and coverage are not independently evaluated in the page.
- The article does not explain how model routing decisions are made or how customers can validate them.

## Provenance Note
This analysis is based only on the captured article text and visible metadata. The capture appears to contain the article’s main body and listed resources, though the surrounding webpage interface and some linked-resource details are not independently assessed.

---

## Key Takeaways

- Azure AI Foundry is presented as an end-to-end platform for building, deploying, monitoring, securing, and governing AI applications and agents.
- The platform is expanding its model catalog with proprietary and open-source models, fine-tuning support, and a developer fine-tuning tier without hosting fees.
- A model router is intended to select suitable Azure OpenAI models, while reserved capacity aims to provide more consistent performance under load.
- Azure AI Foundry Agent Service provides managed infrastructure, orchestration, enterprise-data connectors, templates, and deployment options for workplace platforms.
- Multi-agent workflows use connected agents, A2A communication, and MCP to coordinate complex tasks across clouds and on-premises environments.
- Agentic retrieval in Azure AI Search decomposes complex questions, searches in parallel, and generates cited answers; the article reports early-test relevance gains of up to approximately 40%.
- Observability features are designed to provide metrics, traces, evaluations, CI/CD integration, and production monitoring through Azure Monitor.
- Microsoft Entra Agent ID gives agents distinct organizational identities so administrators can control access and monitor activity.
- Trust features include agent evaluation, red teaming, prompt-injection defenses, guardrails, threat detection, and governance integrations.
- Foundry Local extends AI execution to Windows and Mac devices, supporting offline and edge scenarios, while Azure Arc integration is described as upcoming.

---

## Original Page Content

Software development is undergoing a transformation. In the old world, building software was a long relay—weeks to plan, months to build, and quarters to launch. In the new world, AI-powered tools turn ideas into prototypes in hours and production solutions in days. To achieve this, developers need an end-to-end platform that seamlessly connects code, collaboration, and cloud. Microsoft is the only company where all three come together, with Visual Studio Code, GitHub, and Azure forming a unified, AI-native development experience designed to **empower every developer to shape the future with AI**. We’re delivering a full-stack AI platform with built-in security and trust—giving you everything you need to build and run AI-powered apps and agents, from cloud to edge.

In just two years, we’ve gone from early foundation models to AI agents capable of complex workflows. Microsoft Azure AI Foundry has already grown to support more than 70,000 customers, processing 100 trillion tokens last quarter, and powering 2 billion daily enterprise search queries. What began as an application layer has now become a full-stack platform for building intelligent agents that deliver real business value.

[Design, customize, and manage AI apps with Azure AI Foundry today](https://azure.microsoft.com/en-us/products/ai-foundry)

To help these AI agents become even more powerful and handle more complex tasks, they need state-of-the-art models, integrated tools, and built-in governance. Today at Microsoft Build 2025, we’re unveiling **10 major innovations in Azure AI Foundry** to make this possible.

## 1\. New models

We’re expanding our catalog with cutting-edge models to give developers more choice. This includes [**Grok 3** from xAI](https://aka.ms/grok-announcement) available today, **Flux Pro 1.1** from Black Forest Labs coming soon, and [**Sora coming soon** in preview](https://aka.ms/SoraBuildBlogFinal) via [Azure OpenAI in Foundry Models](https://ai.azure.com/explore/models?selectedCollection=aoai). We now have over [**10,000 open-source models from Hugging Face**](http://aka.ms/FoundryHuggingFace) **available in Foundry Models**. We support [full fine-tuning](https://aka.ms/Build25/FoundryFT) (including LoRA/QLoRA and DPO), so you can tailor fine-tunable models to your needs. Additionally, we’re rolling out [**a new developer tier for fine-tuning—no hosting fees**](https://aka.ms/Build25/FTGlobalAndDev), just a simple way to experiment and evaluate fine-tuning methods without the overhead.

[Learn more about new models in Azure AI Foundry](https://ai.azure.com/explore/models)

![xAI, Hugging Face, and Black Forest Labs logos.](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2025/05/Asset-_1.jpg)

xAI, Hugging Face, and Black Forest Labs logos.

## 2\. Smarter model system

Choosing the right model for each task is now easier. Our new [**model router**](https://aka.ms/AzureAIFoundryModels) automatically selects the optimal Azure OpenAI model for your prompt—boosting quality while reducing costs. Starting next month, we’re extending [**reserved capacity**](https://aka.ms/AzureAIFoundryModels) across Azure OpenAI and select Foundry Models (like models from Black Forest Labs, DeepSeek, Mistral, Meta, and xAI), so you get consistent performance even under heavy load. All these models will be accessible through a unified API and Model Context Protocol (MCP) server for Azure AI Foundry models, making it seamless to go from prototype to production.

[Learn more about model router](https://aka.ms/AzureAIFoundryModels)

![Model router in Azure AI Foundry. ](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2025/05/Asset-2.gif)

Model router in Azure AI Foundry.

## 3\. Azure AI Foundry Agent Service

Azure AI Foundry Agent Service is [now generally available](https://aka.ms/AgentService_ACOM), empowering you to design, deploy, and scale production-grade AI agents with ease. More than **10,000 organizations** —including leaders like [Heineken](https://aka.ms/heinekenazureai), [Carvana](https://aka.ms/carvanastory), and [Fujitsu](https://www.microsoft.com/en/customers/story/21885-fujitsu-azure-ai-foundry) —have already used Azure AI Foundry to automate complex business processes with their own data and knowledge. [This fully managed service](https://aka.ms/Build25/AgentService_GA) takes care of infrastructure and orchestration, and it comes with ready-to-use templates, actions, and connectors to more than **1,400 enterprise data sources** (such as SharePoint, Microsoft Fabric, and third-party systems), speeding up development of context-aware agents. And with a few clicks, you can deploy your agents into Microsoft 365 (Microsoft Teams and Office apps) or other platforms like Slack and Twilio— **bringing agents directly into the tools your employees use every day**. Watch the [Azure AI Foundry Agent Service demo](https://youtu.be/Q1BGjTMuXhE).

[Learn more about Azure AI Foundry Agent Service](https://aka.ms/AgentService_ACOM)

## 4\. Multi-agent orchestration

Real-world workflows often require [multiple agents](https://aka.ms/Build25/Multi-Agent_Workflows) working together. Azure AI Foundry now makes that easy, **across any cloud**. Agents can call each other as tools **(connected agents)**, passing tasks between specialized agents to solve complex problems collaboratively. New **multi-agent workflows** provide a stateful layer to manage context, handle errors, and maintain long-running processes—great for scenarios like financial approvals or supply chain operations. We’ve also implemented **open interoperability standards** —such as **Agent-to-Agent (A2A) communication**, to enable different agents to exchange information and coordinate tasks, and the **Model Context Protocol (MCP)** to enable agents to share and interpret contextual data consistently. These standards ensure agents can **collaborate seamlessly across Azure, AWS, Google Cloud, and on-premises environments**. Under the hood, we are **unifying our Semantic Kernel and AutoGen frameworks** to support this seamless agent orchestration.

And because **Azure AI** **Foundry powers [Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio)**, you maintain a continuous loop—from model selection and fine-tuning to deploying pre-built agents. For instance, **[Stanford Medicine](https://youtu.be/DSOcjyV0oAE)** is already using our healthcare agent orchestrator in Azure AI Foundry alongside Microsoft Copilot Studio to streamline tumor-board meetings with custom clinical workflows.

[Learn more about multi-agent orchestration](https://aka.ms/Build25/Multi-Agent_Workflows)

## 5\. Agentic retrieval

We’re making information retrieval smarter to support these advanced agents. [**Agentic retrieval**](https://aka.ms/AgentRAG) in [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/) is a new multi-turn query engine designed for complex questions. It uses conversation context and an embedded LLM to break down user queries into sub-queries, runs multiple searches in parallel, and then compiles a comprehensive answer with citations. In early tests, this approach [**improves answer relevance by up to ~40%**](https://aka.ms/Build25/aisearch-arevals) on complex, multi-part questions. Now in public preview, agentic retrieval lets your agents **connect to enterprise data more effectively** using advanced retrieval for accurate, grounded answers.

[Learn more about agentic retrieval](https://aka.ms/AgentRAG)

![A screenshot of a diagram](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2025/05/Agentic-retrieval-2048x1152.webp)

A screenshot of a diagram

## 6\. Always-on observability

To hold agents accountable in production, you need visibility into their performance. We’re previewing new [**Foundry Observability**](https://aka.ms/Foundry-Observability) features that provide end-to-end monitoring and diagnostics. You’ll get built-in metrics on latency, throughput, usage, and quality—plus **detailed trace logs** of each agent’s reasoning steps and tool calls. During development, our Agents Playground now shows evaluation benchmarks and traces to help you refine prompts and logic. As you move to CI/CD, we offer integrations with GitHub and Azure DevOps to incorporate tests and guardrails. And in production, a unified dashboard (integrated with Azure Monitor) gives you real-time insight and alerts for your models and agents. Watch the [Azure AI Foundry observability demo](https://youtu.be/SfqjiP_r6Qw).

[Learn more about Foundry Observability](https://aka.ms/Foundry-Observability)

## 7\. Enterprise-grade identity for agents

[Microsoft Entra Agent ID](https://aka.ms/EntraAgentID) is the first step in managing agent identities in your organization, giving you full visibility and control over what your AI agents can do. **Microsoft Entra Agent ID assigns a unique, first-class identity to every agent you build with Azure AI Foundry or Microsoft Copilot Studio**. This means your AI agents get the same identity management as human users—appearing in your Microsoft Entra directory so you can set access controls and permissions for each agent. Soon, security admins will be able to apply Conditional Access policies, multi-factor authentication, and least-privilege roles to agents, and monitor their sign-in activities. If an agent shouldn’t access a resource, it will be blocked just like a regular user would. Watch the [enterprise-grade identity for agents demo](https://youtu.be/137mEB-CyF0).

[Learn more about Microsoft Entra Agent ID](https://aka.ms/EntraAgentID)

## 8\. Trustworthy AI built-in

Responsible AI is non-negotiable for us and our customers. We’ve added new capabilities to **discover, protect, and govern AI systems** from the start. **Agent Evaluators** now automatically check if an agent is following user intent and using tools correctly, flagging issues for developers. An [**AI Red Teaming Agent**](https://devblogs.microsoft.com/foundry/ai-red-teaming-agent-preview/) constantly probes your agents for vulnerabilities or biases, so you can fix weaknesses before deployment. Our content filtering has gotten smarter with [**“Spotlighting”**](https://aka.ms/agenticsecurity-build-25) —an enhancement to **Prompt Shields** that **better detects and mitigates malicious prompt injections** (whether from users or incoming data). We’ve also enabled enhanced [**guardrails**](https://aka.ms/agenticsecurity-build-25) **to prevent agents from revealing sensitive information (PII)** or **straying off approved tasks**. On the [security](https://aka.ms/securityforAI) side, Azure AI Foundry integrates with [**Microsoft Defender for Cloud**](https://www.microsoft.com/en-us/security/business/cloud-security/microsoft-defender-cloud?msockid=00263d999d406b10338028d29cfa6a59) to raise alerts when threats occur. And to help with compliance, we offer **out-of-box integration with governance tools** like **Credo AI**, **Saidot**, and [**Microsoft Purview**](https://www.microsoft.com/en-us/security/business/microsoft-purview) for tracking model performance, fairness, and regulatory requirements. From day one, Azure AI Foundry equips you with the **safety, security, and governance** tools to build AI you (and your users) can trust.

[Learn more about agents security](https://aka.ms/agenticsecurity-build-25)

![A screenshot of a computer](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2025/05/c7f83b8a-1a94-4bb1-af57-0abf0b051c25-2048x1152.webp)

A screenshot of a computer

## 9\. Foundry Local

Not all AI needs to run in the cloud—sometimes the best solution is at the edge. [**Foundry Local**](https://aka.ms/FoundryLocal) is a new runtime for Windows and Mac for **AI models and agents.** With Foundry Local, you can build cross-platform AI apps that work offline, keep sensitive data locally, and reduce bandwidth costs. This opens scenarios like manufacturing on a factory floor with spotty internet, or field service apps that need AI in remote areas. We are also integrating Foundry with Azure Arc. With the upcoming Azure Arc and Foundry integration, you can manage and update on-device AI deployments centrally. In short, **Foundry becomes your AI factory** —delivering generative AI where your data is, whether that’s in the cloud or on-premises. Watch the [Foundry Local demo](https://youtu.be/MZFWfrxzXsE).

[Learn more about Foundry Local](https://aka.ms/FoundryLocal)

## 10\. Future innovations for Foundry Labs

We’re exploring the next frontiers with Microsoft Research in our [**Foundry Labs**](https://ai.azure.com/labs). One exciting invention is **Project Amelie**, powered by RD Agent from Microsoft Research, an autonomous agent that can build complete machine learning pipelines from a single prompt. Give it a task like “predict customer churn from our dataset,” and Amelie will ingest data, train models, and produce a deployable solution—an experiment in AI developing AI.

![A graph on a white surface](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2025/05/f018c144-9930-478e-a565-0993199323dc.webp)

A graph on a white surface

We’re also rethinking how AI agents interact with people and each other: **Magentic-UI**, now open-source, is an experimental human-centered agent that completes web-based tasks, and **TypeAgent** is bringing long-term memory to agents, enabling them to retain and recall knowledge over extended periods. In the scientific realm, new AI models like **EvoDiff** (for generating novel proteins) and **BioEmu** (for predicting how proteins change shape) are being tested in Azure AI Foundry to accelerate research in biology. These forward-looking projects show how Azure AI Foundry is continually innovating—so you’ll always have access to the latest breakthroughs in AI.

[Check out Foundry Labs](https://ai.azure.com/labs)

## The path forward with Azure AI Foundry

**Join us at** [**Microsoft Build 2025**](https://build.microsoft.com/en-US/sessions?search=Azure+AI+Foundry&sortBy=relevance&filter=sessionType%2FlogicalValue%3EBreakout) to see these new capabilities in action and learn how they can transform your business. We’re excited to work with you—our community of developers and customers—to shape this new era of AI. Together, we’re making AI more accessible, powerful, and trustworthy for everyone. Learn more and **get started with [Azure AI Foundry](https://ai.azure.com/)**.

Resources:

- Review [Azure AI Foundry documentation](http://aka.ms/AzureAI).
- Take the [Azure AI Foundry Learn Course](http://aka.ms/learnatbuild).
- Download the [Azure AI Foundry SDK](http://aka.ms/aifoundrysdk).
- Chat with us on [Discord](https://aka.ms/ai/discord).
- Provide feedback on [GitHub](https://aka.ms/azureaifoundry/forum).

---

## Notes


