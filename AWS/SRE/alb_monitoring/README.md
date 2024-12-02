## ALB Monitoring

Application Load Balancer distributes traffic b/w healthy EC2 instances that are registered in a target group. Moreover,
in case of health check failures, the traffic is not routed to the target group - but the account is still charged.

As of now, one possible remediation is to remove the ALB.

### Steps
1. Create a lambda function with file `lambda_function.py`
2. Copy the `policy.json` to the existing policy document attached to lambda's role
3. Configure scheduled trigger w/ EventBridge