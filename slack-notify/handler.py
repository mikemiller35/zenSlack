import os
import json

def lambda_handler(event, context):
    response = {
        "statusCode": 200,
        "headers": {
            "Foo": "bar",
        },
    }
        
    return response