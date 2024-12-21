import boto3
from botocore.exceptions import ClientError
from typing import Optional
import logging

from minerva.config import get_config
from minerva.logging import get_logger
from .types import S3File

class S3Handler:
    """Simple handler for getting files from S3."""
    
    def __init__(self) -> None:
        config = get_config()
        self.logger = get_logger(__name__)
        
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=config.aws_access_key_id,
            aws_secret_access_key=config.aws_secret_access_key
        )
    
    def get_file(self, bucket: str, key: str) -> S3File:
        """
        Get a file from S3 bucket.
        
        Args:
            bucket: Name of the S3 bucket
            key: Path to the file in the bucket
            
        Returns:
            S3File object containing file bytes and metadata
            
        Raises:
            ClientError: If file cannot be retrieved
        """
        try:
            self.logger.debug(f"Fetching file {key} from bucket {bucket}")
            
            # Get the file object
            response = self.s3.get_object(Bucket=bucket, Key=key)
            
            # Read the file content
            file_bytes = response['Body'].read()
            
            # Create S3File object with metadata
            return S3File(
                bytes=file_bytes,
                content_type=response.get('ContentType', 'application/octet-stream'),
                size=response.get('ContentLength', 0),
                last_modified=response.get('LastModified'),
                metadata=response.get('Metadata', {}),
                etag=response.get('ETag', '').strip('"'),
                version_id=response.get('VersionId')
            )
            
        except ClientError as e:
            self.logger.error(f"Failed to get file {key} from bucket {bucket}: {str(e)}")
            raise 