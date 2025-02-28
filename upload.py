import boto3
from botocore.exceptions import ClientError
import os
import sys
import argparse
import requests


s3 = boto3.client('s3', region_name='us-east-1')

def download_file(url, file_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded to {file_path}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading: {e}")

def main():
    FILE_NAME = "new_file"
    url = sys.argv[1]
    bucket_name = sys.argv[2]
    expire_time = sys.argv[3]

    download_file(url, os.path.join(os.getcwd(), FILE_NAME))
    
    resp = s3.put_object(
        Body = FILE_NAME,
        Bucket = bucket_name,
        Key = FILE_NAME
    )
    
    try:
        response = s3.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': FILE_NAME},
                                                    ExpiresIn=expire_time)
    except ClientError as e:
        print(f'Error generating presigned URL: {e}') 
 
    print(f'url: {response}')


if __name__ == "__main__":
    main()

