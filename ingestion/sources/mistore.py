import dlt
from dlt.sources.rest_api import rest_api_resources

from ingestion.sources.templates.shopify import shopify_config


@dlt.source(name="mistore")
def mistore_scraper():
    config = shopify_config("https://mistore.pk")
    yield from rest_api_resources(config)
