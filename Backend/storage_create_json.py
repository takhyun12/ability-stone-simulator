from google.cloud import storage
import json

storage_client = storage.Client.from_service_account_json('Resource/bucket_private_key.json')

BUCKET_NAME = 'craft-log-bucket'
BUCKET = storage_client.get_bucket(BUCKET_NAME)
file_name = 'user_list.json'


def create_json(json_object: dict, file_name: str) -> dict:
    blob = BUCKET.blob(file_name)
    blob.upload_from_string(
        data=json.dumps(json_object),
        content_type='application/json'
    )
    result = file_name + ' upload complete'
    return {'response': result}


user_list = {"users": [
    {
        'name': 'mee',
        'age': '23'
    },
    {
        'name': 'key',
        'age': '22'
    }
]}

user_dict = {'name': 'hello',
             'age': 23}

print(create_json(user_list, file_name))
