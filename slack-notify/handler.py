import os
import json
from botocore.vendored import requests


def lambda_handler(event, context):
    payload = {"text": "Someone hit the endpoint!"}
    slackhook = os.environ.get("SLACKHOOK")
    requests.post(slackhook, json.dumps(payload))

    response = {
        "statusCode": 200,
        "headers": {
            "Foo": "bar",
        },
    }

    return response
