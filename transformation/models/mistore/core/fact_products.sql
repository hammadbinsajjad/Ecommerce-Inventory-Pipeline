{{ config(
        materialized = "table",
        cluster_by = "in_stock",
        partition_by = {
            "field": "publishing_month",
            "data_type": "timestamp",
        },
    ) 
}}

WITH 

products AS (
    SELECT *
    FROM {{ ref("stg_products") }}
),

variants AS (
    SELECT *
    FROM {{ ref("stg_products__variants") }}
)

SELECT *,
    CONCAT("https://mistore.pk/products/", handle) AS url,
    DATE_TRUNC(published_at, MONTH) AS publishing_month,
    CASE WHEN EXISTS((
        SELECT available
        FROM variants
        WHERE available = true
            AND variants.product_id = products.id
    )) THEN true ELSE false END AS in_stock
FROM products
