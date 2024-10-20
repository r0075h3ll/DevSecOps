import logging
import boto3

logger = logging.getLogger()
logger.setLevel("INFO")

ec2_session = boto3.client("ec2", region_name='us-west-2')


def status():
    logger.info("Running status()")
    ids = []

    all_insts = ec2_session.describe_instances()
    logger.info(all_insts)

    print(all_insts['Reservations'])

    for instance in all_insts['Reservations'][0]['Instances']:
        instance_id = instance.get('InstanceId', "unknown")
        keyName = instance.get('KeyName', "unknown")
        state = instance['State'].get("Name", "unknown")

        print("Instance Name: ", keyName)
        print("Instance ID: ", instance_id)
        print("Instance State: ", state)

        if state == "running":
            ids.append(instance_id)

    return ids


def stop_instances(instance_ids: list):
    logger.info("Running stop_instances()")

    try:
        stop_instance = ec2_session.stop_instances(
            InstanceIds=instance_ids, Force=True)
    except Exception as e:
        logger.info(e)
