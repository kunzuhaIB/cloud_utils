import boto3
import logging

def get_client(resource: str) -> boto3.client:
    return boto3.client(resource)

def upload_to_bucket(source_path: str, destination_bucket: str, destination_blob: str, client: boto3.client) -> None:
    """
    Uploads a file to AWS S3 bucket
        directory_path = Path to local directory to upload
        dest_bucket_name = Bucket name in AWS
        dest_blob_name = Directory name in AWS
    """
    try:
        client.upload_file(source_path, destination_bucket, destination_blob)
    except Exception as e:
        logging.Error(f"Error while loading to S3 bucket {destination_bucket}: {e}")