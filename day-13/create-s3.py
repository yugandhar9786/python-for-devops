import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='yuge-demo-boto3-bucket-123'
)
