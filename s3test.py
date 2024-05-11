import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket= 'shiva-demo-bucket-dev-2024',
    CreateBucketConfiguration= {
        'LocationConstraint': 'us-west-2',
    },
)
print(response)