WITH products_data AS (

    SELECT * 
    FROM {{ source("mistore_products", "products") }}

)

SELECT * FROM products_data
