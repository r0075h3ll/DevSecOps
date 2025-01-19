import json

import urllib3

import get_cost

slack_webhook = "https://hooks.slack.com/services/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"


def lambda_handler(event, context):
    usage_report = get_cost.fetch_cost()

    message_body = {
        "text": f"{usage_report}"
    }

    request = urllib3.request('POST', f'{slack_webhook}', body=json.dumps(message_body),
                              headers={"Content-Type": "application/json"})
