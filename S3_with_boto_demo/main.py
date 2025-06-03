from dotenv import load_dotenv
import boto3
import os


# Load env file for AWS Cli authentication
# AWS Cli user required. Configuration: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html

load_dotenv()
# Get credentials from environment variables
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.getenv("AWS_SESSION_TOKEN")  # Optional
# Initialize Boto3 session
session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    aws_session_token=aws_session_token  # Optional
)
s3_client = boto3.client('s3')
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
