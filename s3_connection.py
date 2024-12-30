import os
import boto3
from typing import Optional
from botocore.client import BaseClient

def get_s3_client() -> BaseClient:
    """Get S3 client with credentials from environment.
    
    Returns:
        BaseClient: Boto3 S3 client ready to use
        
    Raises:
        ValueError: If required environment variables missing
        Exception: If connection fails
    """
    # Check required env vars exist
    access_key = os.getenv('AWS_ACCESS_KEY_ID')
    secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    
    if not access_key or not secret_key:
        raise ValueError("AWS credentials not found in environment")
        
    try:
        return boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            endpoint_url=os.getenv('STORAGE_URL')  # Optional custom endpoint
        )
    except Exception as e:
        raise Exception(f"Failed to create S3 client: {str(e)}")

def check_bucket_exists(bucket: str, client: Optional[BaseClient] = None) -> bool:
    """Check if S3 bucket exists and is accessible.
    
    Args:
        bucket: Name of bucket to check
        client: Optional S3 client (creates new one if not provided)
        
    Returns:
        bool: True if bucket exists and is accessible
    """
    s3 = client or get_s3_client()
    try:
        s3.head_bucket(Bucket=bucket)
        return True
    except Exception:
        return False

def get_file_content(bucket: str, key: str, client: Optional[BaseClient] = None) -> str:
    """Get file content from S3 bucket.
    
    Args:
        bucket: Bucket name
        key: File key/path in bucket
        client: Optional S3 client (creates new one if not provided)
        
    Returns:
        str: File content as string
        
    Raises:
        Exception: If file cannot be retrieved
    """
    s3 = client or get_s3_client()
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        return response['Body'].read().decode('utf-8')
    except Exception as e:
        raise Exception(f"Failed to get file {key} from bucket {bucket}: {str(e)}") 