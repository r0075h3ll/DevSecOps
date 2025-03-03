import json
import logging

import requests

import get_cost

slack_webhook = "https://hooks.slack.com/services/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"

logger = logging.getLogger()
logger.setLevel("INFO")


def lambda_handler(event, context):
    usage_report = get_cost.fetch_cost()

    # logger.info(usage_report['ResultsByTime'][0]["Total"].keys())
    logger.info(usage_report.get("ResultsByTime")[0].get("Total").get("AmortizedCost"))
    # return
    cost_inr = float(usage_report.get("ResultsByTime")[0].get("Total").get("AmortizedCost")["Amount"]) * 87.27

    message_body = {
        "blocks": [
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": f"Total cost (INR): {cost_inr}\n\n"
                            }
                        ]
                    },
                    {
                        "type": "rich_text_preformatted",
                        "border": 0,
                        "elements": [
                            {
                                "type": "text",
                                "text": f"{usage_report}"
                            }
                        ]
                    }
                ]
            }
        ]
    }

    # message_body = {
    #     "text": f"{usage_report}"
    # }

    request = requests.post(f'{slack_webhook}', data=json.dumps(message_body),
                            headers={"Content-Type": "application/json"})
