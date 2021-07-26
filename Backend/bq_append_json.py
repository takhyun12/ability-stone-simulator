import os
from google.cloud import bigquery

credentials_path = 'Resource/bigquery_private_key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table_id = 'ability-stone-simulator.craft_log_dataset.test_table'

row_to_insert = [{u'name': 'test_user', u'age': 23}]

errors = client.insert_rows_json(table_id, row_to_insert)
if not errors:
    print('New rows have been added.')
else:
    print(f'Encountered errors while inserting rows: {errors}')