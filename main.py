# This is a sample Python script.
import boto3
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
s3_client = boto3.client('s3')
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
