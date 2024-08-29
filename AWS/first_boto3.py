import boto3

# Initialize the S3 client with a specific region
s3 = boto3.client('s3', region_name='us-east-2')  # Change 'us-east-2' to your desired region

# Create a bucket with the correct location constraint
response = s3.create_bucket(
    Bucket='dfields-boto3-08282024',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'  # Make sure this matches the region above
    }
)

print(response)

