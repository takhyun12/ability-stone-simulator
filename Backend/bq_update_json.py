import os
from google.cloud import bigquery

credentials_path = 'Resource/bigquery_private_key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table_id = 'ability-stone-simulator.craft_log_dataset.test_table'

update_query = """
    UPDATE `ability-stone-simulator.craft_log_dataset.test_table`
    SET name = "11"
    WHERE name = "202"
"""

query_job = client.query(update_query)
query_job.result()

