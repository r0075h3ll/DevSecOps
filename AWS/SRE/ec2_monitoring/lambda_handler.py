import json
from errno import ECHILD

import ec2
import logging

logger = logging.getLogger()
logger.setLevel("INFO")


def lambda_handler(event, context):

    logger.info(event)

    try:
        running_instances = ec2.status()

        if len(running_instances) != 0:
            ec2.stop_instances(running_instances)

        ec2.purge_orphans()
    except Exception as e:
        logger.info(e, exc_info=True)

    return {
        "text": "EC2 Monitoring"
    }
