import os
import json
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError

credentials_path = 'Resource/pubsub_private_key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

timeout = 5.0
subscriber = pubsub_v1.SubscriberClient()
subscription_path = 'projects/ability-stone-simulator/subscriptions/log_topic-sub'


def callback(message):
    # Message
    print(message.data)

    message.ack()

    '''
    if message.attributes:
        for key in message.attributes:
            value = message.attributes.get(key)
            message_dict[key] = value
        print(message_dict)

        # Storage

        crafting_log_path = 'Storage/craft_log.json'
        with open(crafting_log_path, encoding='UTF8') as file:
            json_data = json.load(file)

        json_data['craft_log'].append(message_dict)

        with open(crafting_log_path, mode='w', encoding='UTF8') as file:
            json.dump(json_data, file, indent=4, ensure_ascii=False)
    '''


streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f'Listening for message on {subscription_path}')

with subscriber:
    try:
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel()
        streaming_pull_future.result()
