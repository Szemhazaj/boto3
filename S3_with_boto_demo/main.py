from dotenv import load_dotenv
from log_calls import log_calls
import boto3
import os
import uuid


# Method to create unique bucket name
@log_calls()
def create_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix, str(uuid.uuid4())])


# Load env file for AWS Cli authentication
# AWS Cli user required. Configuration: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html
load_dotenv()
# Get credentials from environment variables
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.getenv("AWS_SESSION_TOKEN")  # Optional
curr_region = "eu-central-1"
# Initialize Boto3 session
session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    # aws_session_token=aws_session_token,  # Optional
    # region_name='curr_region'
)
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3', region_name=curr_region)
bucket_prefix = "boto3-demo-"
for bucket in s3_resource.buckets.filter(BucketRegion=curr_region, Prefix=bucket_prefix):
    print(bucket.name)


bucket_name = create_bucket_name(bucket_prefix)
s3_resource.create_bucket(Bucket=bucket_name,
                          CreateBucketConfiguration={
                              'LocationConstraint': curr_region})

for bucket in s3_resource.buckets.filter(BucketRegion=curr_region, Prefix=bucket_prefix):
    print("--------------Buckets after the execution------------------------")
    print(bucket.name)