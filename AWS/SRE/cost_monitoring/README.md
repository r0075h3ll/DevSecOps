## AWS Cost Monitoring


Pre-requisites:
- Slack App
- AWS Root / Management account

Setup:
- Create a lambda function with these file
	- `lambda_function.py`
	- `slack.py`
- Create a SNS topic
    - Create a subscription for lambda invocation
- Sign in to root/management account
- Create a billing alarm using CloudWatch by configuring the appropriate metrics
    - Select the created SNS topic as target

Get notifications on Slack:
- Create an incoming webhook for your slack app
- Create environment variable for lambda
    - Name: `slack_url`
    - Value: `https://slack_app_webhook_url`
