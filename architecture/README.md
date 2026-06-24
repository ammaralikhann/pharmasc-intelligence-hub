# Architecture

This folder contains architecture and system design documentation for the PharmaSC Intelligence Hub project.

## Files

- `system_design.md`: Explains the high-level architecture, system components, workflow, security considerations, and future enhancements.

## High-Level Flow

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
