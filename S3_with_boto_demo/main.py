from dotenv import load_dotenv
from log_calls import log_calls
import boto3
import os
import uuid


# Method to create unique bucket name
# @log_calls()
def create_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix, str(uuid.uuid4())])


def create_bucket(bucket_prefix, s3_connection):
    session_f = boto3.session.Session()
    current_region = session_f.region_name
    print("Region: ", current_region)
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': current_region})
    print(bucket_name, bucket_response)
    return bucket_name, bucket_response


# Load env file for AWS Cli authentication
# AWS Cli user required. Configuration: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html
load_dotenv()
# Get credentials from environment variables
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.getenv("AWS_SESSION_TOKEN")  # Optional
region = "eu-central-1"



# Initialize Boto3 session
# session = boto3.Session(
#      aws_access_key_id=aws_access_key,
#      aws_secret_access_key=aws_secret_key,
#      # aws_session_token=aws_session_token,  # Optional
#      region_name=region
#  )
# current_region = session.region_name
# print(session.region_name)
# s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3', region_name=region)
bucket_prefix = "boto3-demo-"
for bucket in s3_resource.buckets.filter(BucketRegion=region, Prefix=bucket_prefix):
    print(bucket.name)

for bucket in s3_resource.buckets.filter(BucketRegion=region, Prefix=bucket_prefix):
    print("--------------Buckets after the execution------------------------")
    print(bucket.name)

first_bucket_name, first_response = create_bucket(
    bucket_prefix=bucket_prefix,
    s3_connection=s3_resource)

print(first_response)