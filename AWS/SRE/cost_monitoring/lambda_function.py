import json
import slack


def lambda_handler(event, context):

    msg = slack.payload()
    slack.send_notif(msg)

    return {
        "text": "CloudWatch monitoring"
    }
