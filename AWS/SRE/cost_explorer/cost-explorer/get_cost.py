import datetime

import boto3

cost_client = boto3.client('ce')


def fetch_cost() -> dict:
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)

    usage = cost_client.get_cost_and_usage(
        TimePeriod={
            'Start': yesterday.strftime('%Y-%m-%d'),
            'End': today.strftime('%Y-%m-%d')
        }, Granularity='DAILY', Metrics='AmortizedCost'
    )

    return usage
