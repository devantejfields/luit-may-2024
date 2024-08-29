import boto3  # Import the Boto3 library to interact with AWS services

# Initialize the S3 client (no specific region required here as listing buckets is not region-specific)
s3 = boto3.client('s3')

# Call the list_buckets() method to retrieve a list of all buckets in your AWS account
response = s3.list_buckets()

# Extract the list of buckets from the response dictionary
buckets = response['Buckets']

# Iterate over each bucket in the list
for bucket in buckets:
    # Print the bucket's name and creation date
    print(bucket["Name"], bucket["CreationDate"])
