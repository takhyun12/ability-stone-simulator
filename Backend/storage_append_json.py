from google.cloud import storage
import json

storage_client = storage.Client.from_service_account_json('Resource/bucket_key.json')

BUCKET_NAME = 'craft-log-bucket'
BUCKET = storage_client.get_bucket(BUCKET_NAME)
FILE_NAME = 'user_dict.json'


def get_json():
    blob = BUCKET.get_blob(FILE_NAME)
    json_data = json.loads(blob.download_as_string())
    return json_data


def append_json() -> dict:
    json_data = get_json()

    new_data = {
        'name': 'helloman',
        'age': '22'
    }
    json_data['users'].append(new_data)

    blob = BUCKET.blob(FILE_NAME)
    blob.upload_from_string(
        data=json.dumps(json_data),
        content_type='application/json'
    )
    result = 'upload complete'
    return {'response': result}


response = append_json()
print(response)
