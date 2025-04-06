def shopify_config(base_url, write_disposition="replace", limit=250):
    return {
        "client": {
            "base_url": base_url,
        },
        "resource_defaults": {
            "primary_key": "id",
            "write_disposition": write_disposition,
            "endpoint": {
                "path": "products.json",
                "data_selector": "products",
                "params": {
                    "limit": limit,
                },
                "paginator": {
                    "type": "page_number",
                    "base_page": 1,
                    "total_path": None,
                },
            }
        },
        "resources": [
            "products.json",
        ]
    }
