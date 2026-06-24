# PharmaSC Intelligence Hub

A multi-agent AI supply chain intelligence prototype built using AWS Bedrock, Claude, AWS Lambda, Amazon Athena, and Amazon S3.

## Overview

PharmaSC Intelligence Hub demonstrates how generative AI can support pharmaceutical supply chain planning by identifying inventory, backorder, supplier, logistics, and quality risks.

The project uses sample supply chain datasets, Athena-style SQL queries, Python prototype agents, prompt templates, and a Lambda orchestrator for Amazon Bedrock.

## Business Problem

Supply chain planners often need to review multiple reports and datasets before making decisions.

Common challenges include:

- Low inventory coverage
- Backorder risk
- Supplier delays
- Failed inspections
- High defect rates
- Long replenishment lead times
- High logistics costs
- Manual prioritization of urgent planning actions

This project shows how GenAI can help convert structured supply chain data into clear summaries and recommended actions.

## Key Features

- Inventory and backorder risk detection
- Supplier and logistics risk analysis
- Quality risk identification
- Athena SQL queries for supply chain risk signals
- Python prototype agents for rule-based risk classification
- Prompt templates for Amazon Bedrock
- AWS Lambda orchestrator for Claude model invocation
- Business-friendly recommendation generation
- Recruiter-friendly documentation and walkthrough

## AWS Services Used

- Amazon Bedrock
- Anthropic Claude
- AWS Lambda
- Amazon S3
- Amazon Athena
- Amazon CloudWatch
- AWS IAM

## High-Level Architecture

```text
Sample CSV Data
      ↓
Amazon S3
      ↓
Amazon Athena Queries
      ↓
Python Risk Agents
      ↓
AWS Lambda Orchestrator
      ↓
Amazon Bedrock Claude
      ↓
AI Risk Summary + Recommended Actions
```

## Repository Structure

```text
pharmasc-intelligence-hub/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── sample_data/
│   ├── inventory_backorder_sample.csv
│   ├── supplier_network_sample.csv
│   └── data_dictionary.md
│
├── athena/
│   ├── create_tables.sql
│   └── sample_queries.sql
│
├── prompts/
│   ├── inventory_agent_prompt.md
│   ├── supplier_risk_prompt.md
│   └── recommendation_agent_prompt.md
│
├── agents/
│   ├── inventory_agent.py
│   ├── supplier_risk_agent.py
│   └── recommendation_agent.py
│
├── lambda/
│   ├── bedrock_orchestrator.py
│   └── requirements.txt
│
├── architecture/
│   ├── README.md
│   └── system_design.md
│
└── docs/
    ├── use_case.md
    └── demo_walkthrough.md
```

## Multi-Agent Design

The prototype uses three specialized agents.

### 1. Inventory Agent

Analyzes SKU-level inventory and backorder signals such as:

- National inventory
- Days of supply
- Local backorder quantity
- Forecast demand
- Historical sales
- Supplier/service performance
- Past-due supply

### 2. Supplier Risk Agent

Analyzes supplier, logistics, manufacturing, and quality signals such as:

- Supplier lead time
- Manufacturing lead time
- Inspection result
- Defect rate
- Shipping time
- Transportation route
- Logistics cost

### 3. Recommendation Agent

Combines inventory and supplier findings into prioritized planner actions, leadership escalations, and recommended next steps.

## Example AI Output

```json
{
  "overall_risk_level": "High",
  "executive_summary": "Several SKUs show elevated risk due to low inventory coverage, backorder exposure, and supplier quality issues.",
  "prioritized_actions": [
    {
      "priority": "High",
      "sku": "1591447",
      "issue": "SKU has zero days of supply and has gone on backorder.",
      "recommended_action": "Validate open replenishment orders and escalate potential service impact.",
      "owner": "Planner",
      "timeframe": "Immediate"
    }
  ]
}
```

## How the Demo Works

1. Sample supply chain CSV files are stored in the `sample_data/` folder.
2. Athena SQL scripts define tables and identify risk signals.
3. Python agents classify inventory and supplier risks.
4. Prompt templates guide Bedrock responses.
5. AWS Lambda builds the prompt and invokes Claude through Amazon Bedrock.
6. The system returns an executive summary and prioritized actions.

## Project Documentation

- `docs/use_case.md`
- `docs/demo_walkthrough.md`
- `architecture/system_design.md`
- `sample_data/data_dictionary.md`
- `athena/sample_queries.sql`

## Skills Demonstrated

- Generative AI solution design
- AWS Bedrock integration
- Prompt engineering
- Multi-agent architecture
- Serverless development with AWS Lambda
- Athena SQL querying
- S3 data lake design
- Python development
- Supply chain analytics
- Cloud architecture documentation
- Portfolio project documentation

## Project Status

This is a portfolio prototype project.

The project is designed to demonstrate architecture, business logic, AWS service knowledge, and GenAI workflow design.

## Future Enhancements

Potential future enhancements include:

- Streamlit or React dashboard
- API Gateway endpoint
- Terraform or CloudFormation infrastructure
- CI/CD pipeline
- AWS Glue Data Catalog integration
- Automated S3 ingestion
- Bedrock Guardrails
- Unit tests for Python agents
- Model evaluation framework
- Architecture diagram image
