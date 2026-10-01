# Microsoft Foundry Phase 1 source register

Retrieved or checked: 2026-10-01.

These are current web sources selected for the Phase 1 lesson plan. Microsoft Learn is preferred because the topics include product behavior, roles, networking, deployment types, quotas, and pricing-sensitive decisions.

## Platform and authorization

1. [What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry) — current platform overview and product direction.
2. [Authentication and authorization in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry) — control plane/data plane and Entra ID/API key concepts.
3. [Role-based access control for Microsoft Foundry (Hubs and Projects), classic](https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/hub-rbac-foundry) — hub/project roles and classic hierarchy.

## Networking

4. [Networking options for Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/networking-options) — public, BYO virtual network, and managed virtual network choices.
5. [Configure a managed virtual network for Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/how-to/managed-virtual-network) — isolation modes, outbound rules, private endpoints, limitations, and pricing considerations.
6. [How to configure network isolation for Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link) — private endpoint and inbound/outbound isolation walkthrough.

## Models and deployment

7. [Microsoft Foundry Models overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview) — model categories, catalog, managed compute, serverless, lifecycle, and provider considerations.
8. [Understanding deployment types in Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/deployment-types?view=foundry-classic) — standard, batch, data-zone, regional, provisioned, and developer deployment types.
9. [Compare models using the model leaderboard](https://learn.microsoft.com/en-us/azure/foundry/how-to/benchmark-model-in-catalog) — quality, safety, cost, throughput, feature, and scenario comparisons.

## Economics and controls

10. [Provisioned throughput for Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/provisioned-throughput) — PTU concepts and deployment comparison.
11. [Provisioned throughput billing and cost management](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/provisioned-throughput-onboarding) — hourly capacity billing, utilization, and reservations.
12. [Create and manage budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets) — actual/forecasted budget alerts and their limits.
13. [Use cost alerts to monitor usage and spending](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-alerts-monitor-usage-spending) — alert types and supported account features.

## Source-selection notes

- The original roadmap's “11,000+ models” and “150–200M tokens/month PTU break-even” statements are not carried forward as facts. They depend on current catalog, model, region, workload, pricing, and utilization.
- Azure budgets and cost alerts are notification mechanisms; they do not stop resource consumption.
- The classic Hub/Project material is retained as a compatibility/reference lesson, while the current overview should be used to understand newer Foundry project terminology.
