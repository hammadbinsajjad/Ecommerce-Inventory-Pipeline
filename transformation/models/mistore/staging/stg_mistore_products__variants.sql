WITH variants_data AS (

    SELECT * 
    FROM {{ source("mistore_products", "products__variants") }}

)

select * from variants_data
