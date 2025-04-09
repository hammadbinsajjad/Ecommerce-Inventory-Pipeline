import dlt

from ingestion.sources.mistore import mistore_scraper


def load_mistore():
    pipeline = dlt.pipeline(
        "mistore_pipeline",
        destination="bigquery",
        dataset_name="mistore_products",
    )

    return pipeline.run(mistore_scraper())
