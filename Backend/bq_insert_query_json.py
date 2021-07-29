import os
from google.cloud import bigquery
from datetime import datetime

credentials_path = 'Resource/bigquery_private_key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table_id = 'ability-stone-simulator.test_dataset.payment_table'
time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

'''
insert_query = f"""
    INSERT INTO `{table_id}`(customer_id, license_type, remaining_time, time_refill_date, time_refill_quantity, subscription_date, last_access_time)
    VALUES ("qatester2@onthelive.kr", "Trial", 14400, "{time_stamp}", 14400, "{time_stamp}", "{time_stamp}")
"""
'''
insert_query = f"""
    INSERT INTO `{table_id}`(customer_id, payment_id, payment_date, next_payment_date, amount, currency, order_id)
    VALUES ("admin@onthelive.kr", "P20210729001", "{time_stamp}", "2021-08-29", 3000.0, "KRW", "O20210729001")
"""


print(insert_query)

query_job = client.query(insert_query)
query_job.result()
