import os
import boto3
from typing import Optional, Any
from botocore.client import BaseClient
from .logger import logger
import botocore.exceptions

def get_s3_client() -> BaseClient:
    """Get S3 client with credentials from environment.
    
    Returns:
        BaseClient: Boto3 S3 client ready to use
        
    Raises:
        ValueError: If required environment variables missing
        Exception: If connection fails
    """
    logger.debug("Setting up S3 client")
    
    # Check required env vars exist
    access_key = os.getenv('AWS_ACCESS_KEY_ID')
    secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    
    if not access_key or not secret_key:
        logger.error("AWS credentials not found in environment")
        raise ValueError("AWS credentials not found in environment")
        
    try:
        endpoint_url = os.getenv('STORAGE_URL')
        if endpoint_url:
            logger.debug("Using custom endpoint: %s", endpoint_url)
            
        client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            endpoint_url=endpoint_url
        )
        logger.debug("Successfully created S3 client")
        return client
    except Exception as e:
        logger.error("Failed to create S3 client: %s", str(e))
        raise Exception(f"Failed to create S3 client: {str(e)}")

def check_bucket_exists(bucket: str, client: Optional[BaseClient] = None) -> bool:
    """Check if S3 bucket exists and is accessible.
    
    Args:
        bucket: Name of bucket to check
        client: Optional S3 client (creates new one if not provided)
        
    Returns:
        bool: True if bucket exists and is accessible
    """
    logger.debug("Checking if bucket exists: %s", bucket)
    s3 = client or get_s3_client()
    try:
        s3.head_bucket(Bucket=bucket)
        logger.debug("Bucket exists and is accessible: %s", bucket)
        return True
    except Exception as e:
        logger.warning("Bucket not accessible: %s (%s)", bucket, str(e))
        return False

def get_file_content(bucket: str, key: str, s3: Any) -> str:
    """Get file content from S3 bucket.
    
    Args:
        bucket: Bucket name
        key: File key/path in bucket
        s3: Optional S3 client (creates new one if not provided)
        
    Returns:
        str: File content as string
        
    Raises:
        Exception: If file cannot be retrieved
    """
    logger.debug("Getting file content - bucket: %s, key: %s", bucket, key)
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        return response['Body'].read().decode('utf-8')
    except botocore.exceptions.ClientError as e:
        # Log the error but don't wrap it in a generic Exception
        error_msg = f"Failed to get file {key} from bucket {bucket}: {str(e)}"
        logger.error(error_msg)
        raise  # Re-raise the original ClientError 