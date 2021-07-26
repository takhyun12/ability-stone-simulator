from google.cloud import storage
import json

storage_client = storage.Client.from_service_account_json('Resource/bucket_private_key.json')

BUCKET_NAME = 'craft-log-bucket'
BUCKET = storage_client.get_bucket(BUCKET_NAME)


def get_json(file_name):
    blob = BUCKET.get_blob(file_name)
    json_data = json.loads(blob.download_as_string())
    return json_data


file_name = 'user_dict.json'
json_data = get_json(file_name)
print(json_data)


