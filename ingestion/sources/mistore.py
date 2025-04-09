import dlt
from dlt.sources.rest_api import rest_api_resources

from ingestion.sources.templates.shopify import shopify_config

STORE_NAME = "mistore"

UNWANTED_ATTRIBUTES = [
    "images", "options", "tags",
    "product_type", "body_html",
    "vendor",
]

UNWANTED_VARIANT_ATTRIBUTES = ["featured_image"]


@dlt.source(name="mistore")
def mistore_scraper():
    processing_steps = [
        {"map": remove_unwanted_attributes},
        {"map": remove_unwanted_variant_attributes},
        {"map": add_custom_attributes},
    ]

    config = shopify_config("https://mistore.pk", processing_steps=processing_steps)

    yield from rest_api_resources(config)


def remove_unwanted_attributes(raw_product):
    for attribute in UNWANTED_ATTRIBUTES:
        raw_product.pop(attribute)

    return raw_product


def remove_unwanted_variant_attributes(raw_product):
    for attribute in UNWANTED_VARIANT_ATTRIBUTES:
        for variant in raw_product["variants"]:
            variant.pop(attribute)

    return raw_product


def add_custom_attributes(raw_product):
    raw_product["store_name"] = STORE_NAME
    return raw_product
