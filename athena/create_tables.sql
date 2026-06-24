-- Athena external table definitions for PharmaSC Intelligence Hub
-- Replace the S3 bucket paths with your own bucket locations.

CREATE EXTERNAL TABLE IF NOT EXISTS inventory_backorder_sample (
    sku BIGINT,
    national_inv DOUBLE,
    lead_time DOUBLE,
    in_transit_qty DOUBLE,
    forecast_3_month DOUBLE,
    forecast_6_month DOUBLE,
    forecast_9_month DOUBLE,
    sales_1_month DOUBLE,
    sales_3_month DOUBLE,
    sales_6_month DOUBLE,
    sales_9_month DOUBLE,
    min_bank DOUBLE,
    pieces_past_due DOUBLE,
    perf_6_month_avg DOUBLE,
    perf_12_month_avg DOUBLE,
    local_bo_qty DOUBLE,
    deck_risk STRING,
    went_on_backorder STRING,
    days_of_supply DOUBLE
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar" = "\"",
    "escapeChar" = "\\"
)
LOCATION 's3://your-bucket-name/sample_data/inventory_backorder_sample/'
TBLPROPERTIES (
    "skip.header.line.count" = "1"
);

CREATE EXTERNAL TABLE IF NOT EXISTS supplier_network_sample (
    product_type STRING,
    sku STRING,
    price DOUBLE,
    availability INT,
    number_of_products_sold INT,
    revenue_generated DOUBLE,
    stock_levels INT,
    lead_times INT,
    order_quantities INT,
    shipping_times INT,
    shipping_carriers STRING,
    shipping_costs DOUBLE,
    supplier_name STRING,
    location STRING,
    lead_time INT,
    production_volumes INT,
    manufacturing_lead_time INT,
    manufacturing_costs DOUBLE,
    inspection_results STRING,
    defect_rates DOUBLE,
    transportation_modes STRING,
    routes STRING,
    costs DOUBLE
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar" = "\"",
    "escapeChar" = "\\"
)
LOCATION 's3://your-bucket-name/sample_data/supplier_network_sample/'
TBLPROPERTIES (
    "skip.header.line.count" = "1"
);
