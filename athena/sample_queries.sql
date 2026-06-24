-- Sample Athena queries for PharmaSC Intelligence Hub
-- These queries identify supply chain risk signals that can be passed to Amazon Bedrock.

-- 1. Identify SKUs with_backorder,-- 1. Identify SKUs with immediate backorder risk
    days_of_supply
FROM inventory_backorder_sample
WHERE
    went_on_backorder = 'Yes'
    OR local_bo_qty > 0
    OR days_of_supply <= 7
ORDER BY days_of_supply ASC;

-- 2. Identify SKUs with low or negative inventory
SELECT
    sku,
    national_inv,
    in_transit_qty,
    forecast_3_month,
    sales_3_month,
    min_bank,
    days_of_supply
FROM inventory_backorder_sample
WHERE
    national_inv <= min_bank
    OR national_inv < 0
ORDER BY national_inv ASC;

-- 3. Identify products with high forecast growth versus recent sales
SELECT
    sku,
    forecast_3_month,
    sales_3_month,
    forecast_6_month,
    sales_6_month,
    forecast_9_month,
    sales_9_month
FROM inventory_backorder_sample
WHERE
    forecast_3_month > sales_3_month
    AND forecast_6_month > sales_6_month
ORDER BY forecast_6_month DESC;

-- 4. Identify supplier or service performance concerns
SELECT
    sku,
    lead_time,
    pieces_past_due,
    perf_6_month_avg,
    perf_12_month_avg,
    local_bo_qty,
    went_on_backorder
FROM inventory_backorder_sample
WHERE
    pieces_past_due > 0
    OR perf_6_month_avg < 0.70
    OR perf_12_month_avg < 0.70
ORDER BY perf_6_month_avg ASC;

-- 5. Identify suppliers with long lead times
SELECT
    supplier_name,
    location,
    sku,
    product_type,
    lead_time,
    manufacturing_lead_time,
    shipping_times,
    transportation_modes,
    routes
FROM supplier_network_sample
WHERE
    lead_time >= 20
    OR manufacturing_lead_time >= 20
ORDER BY lead_time DESC;

-- 6. Identify products with quality inspection failures
SELECT
    supplier_name,
    location,
    sku,
    product_type,
    inspection_results,
    defect_rates,
    production_volumes
FROM supplier_network_sample
WHERE
    inspection_results = 'Fail'
    OR defect_rates >= 3.0
ORDER BY defect_rates DESC;

-- 7. Identify high-cost logistics routes
SELECT
    supplier_name,
    location,
    sku,
    transportation_modes,
    routes,
    shipping_carriers,
    shipping_costs,
    costs
FROM supplier_network_sample
WHERE
    costs >= 500
    OR shipping_costs >= 7
ORDER BY costs DESC;

-- 8. Create a combined risk view for AI summarization
SELECT
    i.sku,
    i.national_inv,
    i.forecast_3_month,
    i.sales_3_month,
    i.local_bo_qty,
    i.days_of_supply,
    i.went_on_backorder,
    s.supplier_name,
    s.location,
    s.lead_time AS supplier_lead_time,
    s.inspection_results,
    s.defect_rates,
    s.transportation_modes,
    s.routes
FROM inventory_backorder_sample i
LEFT JOIN supplier_network_sample s
    ON CAST(i.sku AS VARCHAR) = s.sku
WHERE
    i.went_on_backorder = 'Yes'
    OR i.local_bo_qty > 0
    OR i.days_of_supply <= 7
    OR s.inspection_results = 'Fail'
    OR s.defect_rates >= 3.0;
SELECT
    sku,
    national_inv,
    lead_time,
    forecast_3_month,
    sales_3_month,
    local_bo_qty,
    deck_risk,
