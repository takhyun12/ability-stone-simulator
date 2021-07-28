import os
from google.cloud import bigquery

credentials_path = 'Resource/bigquery_private_key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
customer_table_id = 'ability-stone-simulator.test_dataset.customer_table'
payment_table_id = 'ability-stone-simulator.test_dataset.payment_table'

select_query = f"""
SELECT
  customer.customer_id, customer.license_type, customer.remaining_time, customer.time_refill_date, customer.time_refill_quantity, 
  payment.next_payment_date, payment.amount, payment.currency
FROM
  `{customer_table_id}` as customer
INNER JOIN
  `{payment_table_id}` as payment
ON
  customer.customer_id = payment.customer_id
WHERE 
  customer.customer_id = "qatester1@onthelive.kr"
ORDER BY
  order_id;
"""

query_job = client.query(select_query)
query_job.result()

for row in query_job:
    print(row)
