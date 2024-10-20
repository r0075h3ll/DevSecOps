import os
import urllib3
import logging


WEBHOOK_URL = os.getenv("slack_url")
requests = urllib3.PoolManager()


def payload():
    text = {
        "text": "AWS Cost has reached the threshold"
    }

    return text


def send_notif(message: dict):
    try:
        resp = requests.request("POST", WEBHOOK_URL, body=json.dumps(
            message), headers={"Content-Type": "application/json"})
    except Exception as e:
        logger.info(e)

    if resp.status in [200, 201]:
        logger.info("Notification sent successfully!")
    else:
        return {"Status Code": resp.status}
