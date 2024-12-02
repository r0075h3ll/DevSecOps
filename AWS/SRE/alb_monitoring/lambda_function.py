import boto3
import logging

logger = logging.getLogger()
logger.setLevel("INFO")

alb_client = boto3.client("elbv2")
ec2_client = boto3.client("ec2")


def get_albs() -> list:
    logger.info("Running get_albs()")
    all_lbs = alb_client.describe_load_balancers()
    return all_lbs


def probe_albs(albs: list):
    # find all target groups
    logger.info("Running probe_albs()")
    target_group_mapping = {}
    unhealthy_groups = set()

    # for alb in albs:
    #     target_group_mapping[alb.get("LoadBalancerArn", None)] = []

    for alb in albs:
        alb_arn = alb.get("LoadBalancerArn")
        fetch_target_groups = alb_client.describe_target_groups(LoadBalancerArn=alb_arn)
        target_groups = fetch_target_groups.get("TargetGroups")

        for group in target_groups:
            if group.get("Matcher").get("HttpCode") != "200" and group.get("HealthCheckProtocol") == "HTTP":
                unhealthy_groups.update(group.get("my-targets"))

        logger.info(unhealthy_groups)

        if target_groups.__len__() == unhealthy_groups.__len__():
            delete_alb = alb_client.delete_load_balancer(LoadBalancerArn=alb_arn)
            logger.info(delete_alb)

            # target_group_mapping[alb_arn].append(target_group.get)


def lambda_handler():
    try:
        all_lbs = get_albs()
        probe_albs(all_lbs)
    except Exception as e:
        logger.info(e, exc_info=True)
