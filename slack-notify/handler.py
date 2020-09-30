import os
import json
import unzip_requirements
import requests


def lambda_handler(event, context):

    print(event)

    submit_user = json.loads(event.get("body")).get("ticket_quester")

    payload = {"text": "Someone named " + submit_user + " put in a ticket!"}
    slackhook = os.environ.get("SLACKHOOK")
    requests.post(slackhook, json.dumps(payload))

    response = {
        "statusCode": 200,
        "headers": {
            "Posted-To-Slack": "True",
        },
    }

    return response
