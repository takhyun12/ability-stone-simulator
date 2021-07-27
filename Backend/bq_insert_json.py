import os
from google.cloud import bigquery

credentials_path = 'Resource/bigquery_private_key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table_id = 'ability-stone-simulator.test_dataset.test_table'

row_to_insert = [{
    "customer_id": "admin@noiist.ai",
    "license_type": "Admin",
    "remaining_time": 6048000,
    "time_refill_date": "2021-07-26 18:14:28.480028",
    "time_refill_quantity": 6048000,
    "product_id": "",
    "product_name": "",
    "payment_id": "",
    "payment_date": "1900-01-01",
    "next_payment_date": "1900-01-01",
    "amount": 0.0,
    "currency": "",
    "order_id": "",
    "order_date": "1900-01-01"
}]

errors = client.insert_rows_json(table_id, row_to_insert)
if not errors:
    print('New rows have been added.')
else:
    print(f'Encountered errors while inserting rows: {errors}')