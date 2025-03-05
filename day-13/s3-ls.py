import boto3

client = boto3.client('s3')

response = client.list_buckets()

print("existing buckets:")
for bucket in response['Buckets']:
    print(f' {bucket["Name"]}')
