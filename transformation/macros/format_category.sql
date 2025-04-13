{#
    Returns the cleaned and formatted categories
#}

{% macro format_category(product_type) -%}

    INITCAP(COALESCE(NULLIF(RTRIM(product_type), ""), "Empty"))

{%- endmacro %}