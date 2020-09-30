import os
import json
import unzip_requirements
import requests


def lambda_handler(event, context):
    # Slack webhook location
    slackhook = os.environ.get("SLACKHOOK")
    # Data from the Zendesk payload
    submit_user = json.loads(event.get("body")).get("ticket_requester")
    submit_user_email = json.loads(event.get("body")).get("requester_email")
    ticket_url = json.loads(event.get("body")).get("ticket_url")

    # Craft the message to send
    message = ":alert: A ticket came from {} ({}), the ticket is {}".format(
        submit_user, submit_user_email, ticket_url
    )
    # Send our payload to Slack
    payload = {"text": message}
    requests.post(slackhook, json.dumps(payload))

    # Be nice and let Zendesk know we're happy
    response = {
        "statusCode": 200,
        "headers": {
            "Posted-To-Slack": "True",
        },
    }

    return response
