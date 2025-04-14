{{ config(
        materialized = "table",
        cluster_by = "in_stock",
        partition_by = {
            "field": "publishing_month",
            "data_type": "timestamp",
            "granularity": "month",
        },
    ) 
}}

WITH products AS (
    SELECT *
    FROM {{ ref("fact_products") }}
)

SELECT 
    DATE(products.publishing_month) AS publishing_month,
    CASE WHEN in_stock THEN "In Stock" ELSE "Out Of Stock" END AS stock_status,
    {{ format_category("product_type") }} AS category,
FROM products