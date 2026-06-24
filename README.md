# PharmaSC Intelligence Hub

A multi-agent AI supply chain intelligence system built using AWS Bedrock, Claude, Lambda, Athena, and S3.

## Overview

PharmaSC Intelligence Hub is a cloud-based Generative AI prototype designed to help pharmaceutical supply chain teams identify demand, inventory, and supplier risks faster.

The system uses Amazon Bedrock with Claude models to analyze structured supply chain data from Amazon S3 and Amazon Athena, then generates practical business recommendations through multiple specialized AI agents.

## Business Problem

Pharmaceutical supply chains are highly sensitive to demand volatility, inventory shortages, supplier delays, and service-level risk.

Traditional reporting tools can show what happened, but they do not always explain why it matters or what action should be taken.

This project demonstrates how Generative AI can support supply chain planners by summarizing key risks and recommending next-best actions.

## Key Features

- Demand risk summarization
- Inventory shortage detection
- Supplier risk analysis
- AI-generated recommendations
- Athena-based querying over S3 data
- Lambda-based orchestration
- Amazon Bedrock Claude model integration
- Modular multi-agent design

## AWS Services Used

- Amazon Bedrock
- Anthropic Claude Haiku / Claude Sonnet
- AWS Lambda
- Amazon S3
- Amazon Athena
- Amazon CloudWatch
- AWS IAM

## High-Level Architecture

```text
Sample Supply Chain Data
        ↓
Amazon S3 Data Lake
        ↓
Amazon Athena Queries
        ↓
AWS Lambda Orchestrator
        ↓
Amazon Bedrock Claude Model
        ↓
Specialized AI Agents
        ↓
Risk Summary + Recommended Actions
```

## Multi-Agent Design

The solution is organized into specialized agents:

### 1. Demand Agent

Analyzes forecast accuracy, demand spikes, and abnormal demand variance.

### 2. Inventory Agent

Reviews inventory levels, weeks of supply, reorder points, and stockout risk.

### 3. Supplier Risk Agent

Evaluates supplier delays, lead-time risk, and supply continuity concerns.

### 4. Recommendation Agent

Combines the findings from all agents and generates prioritized business actions.

## Example Output

```json
{
  "risk_level": "High",
  "affected_sku": "SKU-102",
  "summary": "Projected demand is above available inventory within the next 3 weeks.",
  "root_cause": "Forecast increase combined with delayed supplier replenishment.",
  "recommended_action": "Expedite supplier purchase order and review allocation strategy for high-priority customers."
}
```

## Skills Demonstrated

- Generative AI solution design
- AWS Bedrock integration
- Prompt engineering
- Serverless architecture
- Supply chain analytics
- Data lake querying with Athena
- Python development
- Cloud documentation
- Multi-agent AI system design

## Project Status

Prototype / portfolio project.

## Future Enhancements

- Add Streamlit dashboard
- Add API Gateway endpoint
- Add Terraform or CloudFormation deployment
- Add automated data ingestion
- Add vector database integration
- Add CI/CD pipeline
- Add unit tests
