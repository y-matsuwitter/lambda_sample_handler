#!-*-coding:utf-8-*-
from __future__ import print_function
import boto3

lmabda_client = boto3.client('lambda')

def lambda_handler(event, context):
    print(event)
    job = event["CodePipeline.job"]["data"]
    target_lambda = job["actionConfiguration"]["configuration"]["UserParameters"]
    artifact = job["inputArtifacts"][0]
    s3Location = artifact["location"]["s3Location"]
    response = lambda_client.update_function_code(
        FunctionName=target_lambda,
        S3Bucket=s3Location["bucketName"],
        S3Key=s3Location["objectKey"],
        Publish=True
    )
    return response
