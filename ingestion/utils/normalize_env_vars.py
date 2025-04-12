import os


def normalize_environment_variables():
    """
        Normalize environment variable
    """

    # Call functions here
    normalize_bigquery_private_key()


def normalize_bigquery_private_key():
    private_key_env_key = "DESTINATION__BIGQUERY__CREDENTIALS__PRIVATE_KEY"

    if big_query_private_key := os.getenv(private_key_env_key, ""):
        os.environ[private_key_env_key] = big_query_private_key.replace("\\n", "\n")
