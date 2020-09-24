import os
import json
import boto3

def lambda_handler(event, context):
    response = {
        "statusCode": 200,
        "headers": {
            "Foo": "bar",
        },
    }
        
    return response