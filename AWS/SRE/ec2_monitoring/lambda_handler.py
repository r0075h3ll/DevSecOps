import json
import ec2
import logging

logger = logging.getLogger()
logger.setLevel("INFO")


def lambda_handler(event, context):

    logger.info(event)

    running_instances = ec2.status()
    ec2.stop_instances(running_instances)

    return {
        "text": "EC2 Monitoring"
    }
