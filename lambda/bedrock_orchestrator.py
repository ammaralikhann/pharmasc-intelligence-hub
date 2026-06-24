"""
AWS Bedrock Lambda Orchestrator

This prototype Lambda function demonstrates how supply chain risk context
could be sent to Amazon Bedrock for AI-generated analysis and recommendations.

The function is designed for portfolio demonstration and should be adapted
with production security, logging, validation, and error handling before use.
"""

import json
import boto3


bedrock_runtime = boto3.client("bedrock-runtime")


def build_bedrock_prompt(event):
    """
    Build a supply chain analysis prompt from the Lambda event payload.
    """

    inventory_findings = event.get("inventory_findings", [])
    supplier_findings = event.get("supplier_findings", [])

    prompt = f"""
You are a pharmaceutical supply chain intelligence assistant.

Analyze the following inventory and supplier risk findings and generate
a concise executive summary with prioritized recommendations.

Inventory Findings:
{json.dumps(inventory_findings, indent=2)}

Supplier Findings:
{json.dumps(supplier_findings, indent=2)}

Return the response in JSON format with:
- overall_risk_level
- executive_summary
- prioritized_actions
- leadership_escalations
- missing_information
"""

    return prompt


def invoke_bedrock_claude(prompt):
    """
    Invoke Anthropic Claude on Amazon Bedrock.

    Model ID can be changed based on availability and cost/performance needs.
    """

    request_body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 800,
        "temperature": 0.2,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
    }

    response = bedrock_runtime.invoke_model(
        modelId="anthropic.claude-3-haiku-20240307-v1:0",
        body=json.dumps(request_body),
        contentType="application/json",
        accept="application/json",
    )

    response_body = json.loads(response["body"].read())

    return response_body


def lambda_handler(event, context):
    """
    AWS Lambda entry point.
    """

    try:
        prompt = build_bedrock_prompt(event)
        bedrock_response = invoke_bedrock_claude(prompt)

        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": "Supply chain intelligence summary generated successfully.",
                    "bedrock_response": bedrock_response,
                }
            ),
        }

    except Exception as error:
        return {
            "statusCode": 500,
            "body": json.dumps(
                {
                    "message": "Failed to generate supply chain intelligence summary.",
                    "error": str(error),
                }
            ),
        }
