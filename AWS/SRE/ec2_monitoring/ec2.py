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

def create_ebs_snapshot(orphans: set):
    logger.info("Running create_ebs_snapshot()")

    for vol in orphans:
        ec2_session.create_snapshot(Description=f"{vol} backup",VolumeId=vol)

def purge_orphans():
    logger.info("Running remove_orphans()")
    volumes = ec2_session.describe_volumes()

    logger.info(volumes)

    orphans = set()

    for vol in volumes["Volumes"]:
        volume_id = vol["VolumeId"]

        print("Volume ID: %s" % volume_id)
        print("Volume Type: %s" % vol["VolumeType"])
        print("Volume AZ: %s" % vol["AvailabilityZone"])

        if (vol["Attachments"][0].get("InstanceId", False)) is False and vol["State"] == "available":
            orphans.add(volume_id)

    if orphans.__len__() != 0:
        logger.info("Creating snapshots")
        create_ebs_snapshot(orphans)

        for v_id in orphans:
            logger.info("Deleted %s" %
            v_id)
            resp = ec2_session.delete_volume(VolumeID=v_id)

            logger.info(resp)
    else:
        logger.info("No orphaned EBS volumes")