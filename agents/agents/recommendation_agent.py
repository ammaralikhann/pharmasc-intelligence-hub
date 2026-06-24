"""
Recommendation Agent

This prototype agent converts inventory and supplier risk findings into
prioritized business actions for supply chain planners.

In a production AWS Bedrock workflow, this logic could be combined with
foundation model summarization to create executive-level recommendations.
"""


def assign_owner(risk_finding):
    """
    Assign a likely business owner based on the type of risk.
    """

    if "supplier_name" in risk_finding:
        return "Supplier Manager"

    if risk_finding.get("local_bo_qty", 0) and float(risk_finding["local_bo_qty"]) > 0:
        return "Planner"

    if risk_finding.get("days_of_supply", 999) and float(risk_finding["days_of_supply"]) <= 7:
        return "Planner"

    return "Supply Chain Manager"


def assign_timeframe(risk_level):
    """
    Assign an action timeframe based on risk severity.
    """

    if risk_level == "High":
        return "Immediate"

    if risk_level == "Medium":
        return "This week"

    return "Monitor"


def build_recommendation(risk_finding):
    """
    Build a prioritized recommendation from a risk finding.
    """

    risk_level = risk_finding.get("risk_level", "Low")
    sku = risk_finding.get("sku", "Unknown SKU")
    owner = assign_owner(risk_finding)
    timeframe = assign_timeframe(risk_level)

    if risk_level == "High":
        action = (
            "Escalate risk, validate available supply, review open orders, "
            "and create a recovery plan."
        )
    elif risk_level == "Medium":
        action = (
            "Monitor risk closely, confirm next replenishment timing, "
            "and review planning assumptions."
        )
    else:
        action = "Continue monitoring through the standard planning process."

    return {
        "priority": risk_level,
        "sku": sku,
        "issue": risk_finding,
        "recommended_action": action,
        "owner": owner,
        "timeframe": timeframe,
    }


def generate_recommendations(inventory_findings, supplier_findings):
    """
    Combine inventory and supplier findings into prioritized recommendations.
    """

    combined_findings = inventory_findings + supplier_findings

    recommendations = [
        build_recommendation(finding) for finding in combined_findings
    ]

    priority_order = {"High": 1, "Medium": 2, "Low": 3}

    recommendations.sort(
        key=lambda item: priority_order.get(item["priority"], 3)
    )

    return recommendations


if __name__ == "__main__":
    inventory_findings = [
        {
            "sku": "1591447",
            "risk_level": "High",
            "national_inv": 0,
            "days_of_supply": 0,
            "local_bo_qty": 0,
            "went_on_backorder": "Yes",
        }
    ]

    supplier_findings = [
        {
            "supplier_name": "Supplier 5",
            "sku": "SKU3",
            "risk_level": "High",
            "lead_time": 24,
            "inspection_results": "Fail",
            "defect_rates": 4.75,
        }
    ]

    results = generate_recommendations(inventory_findings, supplier_findings)

    for result in results:
        print(result)
