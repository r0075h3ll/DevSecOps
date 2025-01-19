import json

import urllib3

import get_cost


def lambda_handler(event, context):
    usage_report = get_cost.fetch_cost()

    message_body = {
        "text": f"{usage_report}"
    }

    request = urllib3.request('POST', 'slack_webhook_url', body=json.dumps(message_body),
                              headers={"Content-Type": "application/json"})
