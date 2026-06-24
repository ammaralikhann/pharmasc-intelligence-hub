"""
Inventory Agent

This prototype agent identifies inventory and backorder risk signals from
SKU-level supply chain records.

The logic is intentionally simple for portfolio demonstration. In a production
AWS Bedrock workflow, this output could be passed into a prompt template and
summarized by a foundation model.
"""


def classify_inventory_risk(record):
    """
    Classify the inventory risk level for one SKU record.
    """

    national_inv = float(record.get("national_inv", 0))
    min_bank = float(record.get("min_bank", 0))
    local_bo_qty = float(record.get("local_bo_qty", 0))
    days_of_supply = float(record.get("days_of_supply", 999))
    pieces_past_due = float(record.get("pieces_past_due", 0))
    perf_6_month_avg = float(record.get("perf_6_month_avg", 1))
    went_on_backorder = str(record.get("went_on_backorder", "No")).lower()

    if (
        went_on_backorder == "yes"
        or local_bo_qty > 0
        or days_of_supply <= 7
        or national_inv < 0
    ):
        return "High"

    if (
        days_of_supply <= 30
        or national_inv <= min_bank
        or pieces_past_due > 0
        or perf_6_month_avg < 0.70
    ):
        return "Medium"

    return "Low"


def analyze_inventory_records(records):
    """
    Analyze multiple inventory records and return prioritized risk findings.
    """

    findings = []

    for record in records:
        risk_level = classify_inventory_risk(record)

        if risk_level in ["High", "Medium"]:
            findings.append(
                {
                    "sku": record.get("sku"),
                    "risk_level": risk_level,
                    "national_inv": record.get("national_inv"),
                    "days_of_supply": record.get("days_of_supply"),
                    "local_bo_qty": record.get("local_bo_qty"),
                    "went_on_backorder": record.get("went_on_backorder"),
                    "recommended_action": build_inventory_recommendation(
                        record, risk_level
                    ),
                }
            )

    risk_priority = {"High": 1, "Medium": 2, "Low": 3}
    findings.sort(key=lambda item: risk_priority[item["risk_level"]])

    return findings


def build_inventory_recommendation(record, risk_level):
    """
    Generate a simple planner-facing recommendation.
    """

    if risk_level == "High":
        return (
            "Review replenishment immediately, validate open supply, "
            "and escalate if customer service impact is expected."
        )

    if risk_level == "Medium":
        return (
            "Monitor inventory position, review forecast assumptions, "
            "and confirm supplier delivery timing."
        )

    return "Continue monitoring under standard planning process."


if __name__ == "__main__":
    sample_records = [
        {
            "sku": "1591447",
            "national_inv": 0,
            "min_bank": 0,
            "local_bo_qty": 0,
            "days_of_supply": 0,
            "pieces_past_due": 0,
            "perf_6_month_avg": 0.00,
            "went_on_backorder": "Yes",
        },
        {
            "sku": "3176426",
            "national_inv": 10,
            "min_bank": 0,
            "local_bo_qty": 0,
            "days_of_supply": 999,
            "pieces_past_due": 0,
            "perf_6_month_avg": 0.00,
            "went_on_backorder": "No",
        },
    ]

    results = analyze_inventory_records(sample_records)

    for result in results:
        print(result)
