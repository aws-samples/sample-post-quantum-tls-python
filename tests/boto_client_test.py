import boto3

REGION = "ap-southeast-1"

secretsmanager = boto3.client("secretsmanager", region_name=REGION)
assert secretsmanager.list_secrets()["ResponseMetadata"]["HTTPStatusCode"] == 200
print("ok")
