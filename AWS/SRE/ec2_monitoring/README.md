## EC2 Monitoring

Steps:
- Create a lambda function with these file
	- `lambda_function.py`
	- `ec2.py`
- Attach inline policy i.e. `policy.json` to the lambda role 
- Create scheduled trigger in EventBridge for lambda invocation
	- Sample Cron Expression: `20 0 * * ? *`


Features
- [x] Stop all instances