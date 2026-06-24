# Demo Walkthrough

## Overview

This walkthrough explains how the PharmaSC Intelligence Hub prototype works from data input to AI-generated recommendations.

The project demonstrates a serverless GenAI workflow using:

- Sample supply chain CSV data
- Amazon S3
- Amazon Athena
- AWS Lambda
- Amazon Bedrock
- Python prototype agents
- Prompt templates

## Demo Objective

The goal of the demo is to show how supply chain risk data can be converted into clear, prioritized recommendations for planners and supply chain leaders.

## Step 1: Review Sample Data

The project includes two sample datasets:

```text
sample_data/
├── inventory_backorder_sample.csv
└── supplier_network_sample.csv
