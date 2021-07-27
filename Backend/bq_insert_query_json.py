import os
from google.cloud import bigquery

credentials_path = 'Resource/bigquery_private_key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table_id = 'ability-stone-simulator.craft_log_dataset.test_table'

select_query = """
    SELECT *
    FROM `ability-stone-simulator.craft_log_dataset.test_table`
"""

query_job = client.query(select_query)
query_job.result()
for row in query_job:
    print("name={}, age={}".format(row[0], row[1]))