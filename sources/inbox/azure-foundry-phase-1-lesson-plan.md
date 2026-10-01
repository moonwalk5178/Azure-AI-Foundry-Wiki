# Microsoft Foundry Phase 1 lesson plan: platform architecture and economics

**Purpose:** Build enough platform, governance, networking, model-selection, and cost knowledge to make a defensible design for a small Microsoft Foundry application.

**Suggested pace:** 3–5 hours per week for four weeks.

**Prerequisites:** Basic Azure concepts (subscriptions, resource groups, identity, and regions), familiarity with cloud networking, and basic Python or REST knowledge.

## Learning outcome

At the end of the four weeks, produce a short architecture and cost brief containing:

1. A control-plane/data-plane and resource/project diagram.
2. A least-privilege identity and RBAC matrix.
3. A network decision record covering inbound and outbound paths.
4. A model and deployment comparison.
5. A low/expected/high cost estimate and guardrail plan.

Label sourced facts, personal calculations, and unresolved questions separately.

## Week 1 — Platform boundaries, identity, and governance

### Read

- [What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry)
- [Authentication and authorization in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry)
- [Role-based access control for Microsoft Foundry (Hubs and Projects), classic](https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/hub-rbac-foundry)

### Study

Understand the difference between Azure control-plane actions and Foundry data-plane actions, Microsoft Entra ID versus API keys, and resource, hub, and project scopes. Hub/Project remains useful for classic environments, but the current overview says new investments focus on Foundry projects in the new portal.

### Practice

Draw the resource relationships for a small Foundry application. Create a role matrix for an administrator, developer, and read-only reviewer. For each action—creating resources, assigning permissions, deploying a model, running inference, and viewing telemetry—identify the scope and authorization surface.

### Checkpoint

Explain who can perform each action, at which scope, and whether it is a control-plane or data-plane operation.

## Week 2 — Network isolation and data paths

### Read

- [Networking options for Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/networking-options)
- [Configure a managed virtual network for Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/how-to/managed-virtual-network)
- [How to configure network isolation for Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link)

### Study

Compare public egress, a customer-managed (BYO) virtual network, and a Microsoft-managed virtual network. Separate inbound endpoint protection from outbound data egress. Note region support, private endpoints, managed identity permissions, private DNS, firewall behavior, and the limitations of each option.

### Practice

Draw inbound and outbound paths for Foundry, Storage, Azure AI Search, Key Vault, and the model endpoint. Mark which traffic is public, private, or controlled by an allow-list. Record likely operational and cost consequences.

### Safety note

Use a disposable environment for hands-on network changes. Read the limitations before enabling isolation; do not experiment first in a production subscription.

### Checkpoint

Choose a network pattern for the retail-agent capstone and justify it using data exposure, connectivity, regional requirements, operations, and cost.

## Week 3 — Model selection and deployment types

### Read

- [Microsoft Foundry Models overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview)
- [Understanding deployment types in Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/deployment-types?view=foundry-classic)
- [Compare models using the model leaderboard](https://learn.microsoft.com/en-us/azure/foundry/how-to/benchmark-model-in-catalog)

### Study

Learn the difference between models sold by Azure and partner/community models, managed compute and serverless deployment, and standard, batch, data-zone, regional, provisioned, and developer deployment types. Pay attention to region, data processing, SLA, lifecycle, feature support, licensing, and billing.

### Practice

Compare three candidate models against the same small test set. Record quality, safety, latency or throughput, context window, tool/structured-output support, region availability, lifecycle status, licensing/provider constraints, and estimated cost. Make one recommendation for development and another for a predictable production workload.

### Checkpoint

Document what evidence would change your model or deployment choice. Do not use the original roadmap's model-count headline as a selection criterion.

## Week 4 — Economics, quotas, and guardrails

### Read

- [Provisioned throughput for Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/provisioned-throughput)
- [Provisioned throughput billing and cost management](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/provisioned-throughput-onboarding)
- [Create and manage budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)
- [Use cost alerts to monitor usage and spending](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-alerts-monitor-usage-spending)

### Study

Compare variable token billing with reserved PTU capacity using measured tokens-per-minute, utilization, latency requirements, capacity, region, and model-specific pricing. Include managed compute, storage, search, networking, monitoring, and other supporting services in the estimate.

### Practice

Build a low/expected/high monthly estimate. Add a budget, actual and forecasted alerts, ownership for each alert, quota review, rate/token limits, deployment cleanup, resource tags, and application-level rate limiting.

### Important distinction

Azure budgets and cost alerts notify people; they do not stop resource consumption. Treat them as detection and accountability controls. Design separate preventative controls through quotas, access restrictions, deployment policies, and application-level limits.

### Checkpoint

Submit a one-page cost and guardrail brief with assumptions, a PTU utilization threshold, a cleanup plan, and the conditions under which PAYG or PTU is preferable.

## Final review exercise

Use the retail-agent capstone as the scenario: synthetic HR-policy documents plus mock inventory and pricing data. Package the five artifacts from the learning outcome and mark every claim as one of:

- **Sourced fact** — supported by current Microsoft documentation.
- **Calculation** — derived from stated workload and pricing assumptions.
- **Design choice** — a decision with stated trade-offs.
- **Open question** — requires validation in the target subscription, region, model, or tenant.

Avoid universal PTU break-even claims. The original roadmap's numeric claims should be treated as hypotheses until current pricing, model availability, quotas, and regional behavior are checked.
