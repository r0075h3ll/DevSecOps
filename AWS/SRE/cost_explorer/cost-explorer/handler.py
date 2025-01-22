import json

import requests

import get_cost

slack_webhook = "<slack_webhook_url>"


def lambda_handler(event, context):
    usage_report = get_cost.fetch_cost()

    message_body = {
        "text": f"{usage_report}"
    }

    request = requests.post(f'{slack_webhook}', data=json.dumps(message_body),
                              headers={"Content-Type": "application/json"})
