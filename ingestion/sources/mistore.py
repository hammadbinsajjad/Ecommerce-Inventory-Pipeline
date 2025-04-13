import dlt
from dlt.sources.rest_api import rest_api_resources

from ingestion.sources.templates.shopify import shopify_config

STORE_ID = "mistore"

UNWANTED_ATTRIBUTES = [
    "images", "options", "tags",
    "body_html", "vendor",
]

UNWANTED_VARIANT_ATTRIBUTES = ["featured_image"]


@dlt.source(name="mistore")
def mistore_scraper():
    processing_steps = [
        {"map": add_custom_attributes},
        {"map": remove_unwanted_attributes},
        {"map": remove_unwanted_variant_attributes},
    ]

    config = shopify_config("https://mistore.pk", processing_steps=processing_steps)

    yield from rest_api_resources(config)


def remove_unwanted_attributes(raw_product):
    for attribute in UNWANTED_ATTRIBUTES:
        raw_product.pop(attribute)

    return raw_product


def remove_unwanted_variant_attributes(raw_product):
    for attribute in UNWANTED_VARIANT_ATTRIBUTES:
        for raw_variant in raw_product["variants"]:
            raw_variant.pop(attribute)

    return raw_product


def add_custom_attributes(raw_product):
    raw_product["store_id"] = STORE_ID
    return raw_product
