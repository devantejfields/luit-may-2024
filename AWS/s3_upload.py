import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Specify the path to your file
file_path = "test_text.txt"  # Update this path if the file is in a different location

    # Open the file in binary read mode
with open(file_path, 'rb') as f:
        # Upload the file to an S3 bucket
     s3.upload_fileobj(f, 'dfields-boto3-08282024 ', 'test_text.txt')