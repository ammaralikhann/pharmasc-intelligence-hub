"""
Supplier Risk Agent

This prototype agent identifies supplier, logistics, manufacturing, and quality
risk signals from supplier network records.

The logic is intentionally simple for portfolio demonstration. In a production
AWS Bedrock workflow, this output could be passed into a prompt template and
summarized by a foundation model.
"""


def classify_supplier_risk(record):
    """
    Classify supplier risk level for one supplier/SKU record.
    """

    availability = float(record.get("availability", 999))
    stock_levels = float(record.get("stock_levels", 999))
    lead_time = float(record.get("lead_time", 0))
    manufacturing_lead_time = float(record.get("manufacturing_lead_time", 0))
    shipping_times = float(record.get("shipping_times", 0))
    shipping_costs = float(record.get("shipping_costs", 0))
    route_costs = float(record.get("costs", 0))
    defect_rates = float(record.get("defect_rates", 0))
    inspection_results = str(record.get("inspection_results", "")).lower()

    if (
        inspection_results == "fail"
        or defect_rates >= 3.0
        or lead_time >= 20
        or manufacturing_lead_time >= 20
        or stock_levels <= 10
    ):
        return "High"

    if (
        shipping_times >= 7
        or shipping_costs >= 7
        or route_costs >= 500
        or availability <= 30
    ):
        return "Medium"

    return "Low"


def analyze_supplier_records(records):
    """
    Analyze multiple supplier records and return prioritized risk findings.
    """

    findings = []

    for record in records:
        risk_level = classify_supplier_risk(record)

        if risk_level in ["High", "Medium"]:
            findings.append(
                {
                    "supplier_name": record.get("supplier_name"),
                    "sku": record.get("sku"),
                    "product_type": record.get("product_type"),
                    "location": record.get("location"),
                    "risk_level": risk_level,
                    "lead_time": record.get("lead_time"),
                    "inspection_results": record.get("inspection_results"),
                    "defect_rates": record.get("defect_rates"),
                    "recommended_action": build_supplier_recommendation(
                        record, risk_level
                    ),
                }
            )

    risk_priority = {"High": 1, "Medium": 2, "Low": 3}
    findings.sort(key=lambda item: risk_priority[item["risk_level"]])

    return findings


def build_supplier_recommendation(record, risk_level):
    """
    Generate a simple planner-facing supplier risk recommendation.
    """

    if risk_level == "High":
        return (
            "Escalate supplier risk, validate recovery timing, "
            "and evaluate alternate supply or allocation options."
        )

    if risk_level == "Medium":
        return (
            "Monitor supplier performance, confirm shipment timing, "
            "and review cost or route exposure."
        )

    return "Continue monitoring supplier under standard planning process."


if __name__ == "__main__":
    sample_records = [
        {
            "supplier_name": "Supplier 5",
            "sku": "SKU3",
            "product_type": "skincare",
            "location": "Kolkata",
            "availability": 68,
            "stock_levels": 23,
            "lead_time": 24,
            "manufacturing_lead_time": 18,
            "shipping_times": 6,
            "shipping_costs": 1.73,
            "inspection_results": "Fail",
            "defect_rates": 4.75,
            "costs": 254.78,
        },
        {
            "supplier_name": "Supplier 4",
            "sku": "SKU7",
            "product_type": "cosmetics",
            "location": "Bangalore",
            "availability": 59,
            "stock_levels": 93,
            "lead_time": 22,
            "manufacturing_lead_time": 1,
            "shipping_times": 1,
            "shipping_costs": 2.35,
            "inspection_results": "Fail",
            "defect_rates": 0.40,
            "costs": 802.06,
        },
    ]

    results = analyze_supplier_records(sample_records)

    for result in results:
        print(result)
``
