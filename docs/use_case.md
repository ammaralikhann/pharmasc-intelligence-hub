# Use Case: AI-Powered Supply Chain Risk Intelligence

## Overview

PharmaSC Intelligence Hub demonstrates how generative AI can help supply chain planners identify and summarize inventory, backorder, supplier, logistics, and quality risks.

The project uses sample supply chain datasets, Athena-style SQL queries, Python prototype agents, and an AWS Bedrock Lambda orchestrator to simulate an AI-assisted planning workflow.

## Business Problem

Supply chain planners often need to review multiple datasets before making decisions, including:

- Inventory positions
- Forecast demand
- Historical sales
- Backorder quantities
- Supplier lead times
- Supplier performance
- Quality inspection results
- Logistics costs
- Transportation routes

This process can be manual, time-consuming, and difficult to prioritize.

## Target Users

The intended users are:

- Supply chain planners
- Inventory planners
- Supplier managers
- Logistics analysts
- Supply chain leaders

## Key Questions Answered

The system is designed to help answer questions such as:

1. Which SKUs are most at risk of backorder?
2. Which products have low or negative days of supply?
3. Which suppliers have long lead times?
4. Which products have quality inspection failures?
5. Which routes or carriers have high logistics cost?
6. Which issues require immediate planner action?
7. Which risks should be escalated to leadership?

## Proposed Solution

The solution combines structured analytics with generative AI:

1. Store supply chain CSV files in Amazon S3.
2. Use Amazon Athena to query inventory and supplier risk signals.
3. Use AWS Lambda to orchestrate agent logic and prompt generation.
4. Use Amazon Bedrock with Claude to summarize findings.
5. Generate prioritized actions for planners and leaders.

## Example Scenario

A planner needs to review weekly supply chain risk.

The planner uploads or receives updated CSV extracts containing:

- Inventory and backorder data
- Supplier network data
- Quality and logistics data

Athena queries identify records with high-risk signals, such as:

- Backorder status equals Yes
- Local backorder quantity greater than zero
- Days of supply less than or equal to 7
- Supplier inspection result equals Fail
- Defect rate greater than or equal to 3 percent
- Supplier lead time greater than or equal to 20 days

The Lambda orchestrator sends the risk records to Amazon Bedrock.

The AI model generates:

- Executive risk summary
- Prioritized SKU actions
- Supplier risk mitigation recommendations
- Leadership escalation items
- Missing data requirements

## Example Business Output

```json
{
  "overall_risk_level": "High",
  "executive_summary": "Several SKUs show elevated risk due to low inventory coverage, backorder exposure, and supplier quality issues.",
  "prioritized_actions": [
    {
      "priority": "High",
      "sku": "1591447",
      "issue": "SKU has zero days of supply and has gone on backorder.",
      "recommended_action": "Validate open replenishment orders and escalate potential customer service impact.",
      "owner": "Planner",
      "timeframe": "Immediate"
    },
    {
      "priority": "High",
      "sku": "SKU3",
      "issue": "Supplier inspection failed and defect rate is elevated.",
      "recommended_action": "Escalate with supplier quality team and evaluate alternate supply options.",
      "owner": "Supplier Manager",
      "timeframe": "Immediate"
    }
  ]
}
