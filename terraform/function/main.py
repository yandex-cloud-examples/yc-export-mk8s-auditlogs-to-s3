import boto3
import json
import os
import random
import string
from datetime import datetime

# Variables
config = {
    'bucket_name'      : os.environ['BUCKET_NAME'],
}

# Function - Random string
def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result

# Boto client
client = boto3.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net',
    region_name='ru-central1'
)

# Handler
def handler(event, context):
    for log_data in event['messages']:

        full_log = []
        for log_entry in log_data['details']['messages']:
            # Temporary filter
            try:
                if (log_entry['json_payload']['apiVersion'] == "audit.k8s.io/v1"):
                    full_log.append(json.dumps(log_entry))
                else:
                    print("wrong apiVersion key")
            except KeyError:
                print("no apiVersion key")
            # Temporary filter end

        object_key = 'AUDIT/'+datetime.now().strftime('%Y-%m-%d-%H:%M:%S')+'-'+get_random_alphanumeric_string(5)
        object_value = '\n'.join(full_log)
        client.put_object(Bucket=config['bucket_name'], Key=object_key, Body=object_value)
        print(object_value)