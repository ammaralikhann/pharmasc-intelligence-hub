# System Design

## Project Name

PharmaSC Intelligence Hub

## Purpose

PharmaSC Intelligence Hub is a portfolio prototype that demonstrates how generative AI can support pharmaceutical supply chain planning.

The system is designed to analyze inventory, backorder, supplier, logistics, and quality risk signals, then generate planner-friendly recommendations using Amazon Bedrock.

## Business Problem

Supply chain planners often work across multiple reports, spreadsheets, systems, and supplier updates. This can make it difficult to quickly identify which SKUs require urgent attention.

Common planning challenges include:

- Low inventory coverage
- Backorder risk
- Long supplier lead times
- Failed inspections
- High defect rates
- Delayed replenishment
- High logistics cost
- Limited visibility across demand, inventory, and supplier signals

This project shows how a GenAI-based workflow can help convert structured supply chain data into risk summaries and recommended actions.

## High-Level Architecture

```text
Sample CSV Data
      ↓
Amazon S3
      ↓
Amazon Athena
      ↓
AWS Lambda Orchestrator
      ↓
Amazon Bedrock Claude Model
      ↓
Specialized AI Agents
      ↓
Risk Summary + Recommended Actions
