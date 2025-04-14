{{ config(
        materialized = "table",
        cluster_by = "stock_status",
        partition_by = {
            "field": "publishing_month",
            "data_type": "date",
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