import os
from s3_connection import get_s3_client, check_bucket_exists
from dotenv import load_dotenv
from logger import logger

# Load environment variables 
load_dotenv()

def upload_test_file():
    # Get bucket name from env
    bucket = os.getenv('BUCKET_NAME')
    if not bucket:
        logger.error("BUCKET_NAME environment variable not set")
        return False

    # Check bucket exists
    s3_client = get_s3_client()
    if not check_bucket_exists(bucket, s3_client):
        logger.error("Bucket '%s' not found or not accessible", bucket)
        logger.error("Check your credentials and bucket name")
        return False

    logger.info("Creating test markdown content")
    # Create simple test markdown content
    test_content = """# Test Document

This is a test markdown file.
It contains some simple content to verify uploading works.

## Section 1
- Bullet point 1
- Bullet point 2

## Section 2
Some regular paragraph text."""

    # Upload the file
    try:
        file_key = "test_doc.md"
        logger.debug("Uploading test file to %s/%s", bucket, file_key)
        s3_client.put_object(
            Bucket=bucket,
            Key=file_key,
            Body=test_content,
            ContentType='text/markdown'
        )
        logger.info("Successfully uploaded test file to %s/%s", bucket, file_key)
        return True
    except Exception as e:
        logger.error("Failed to upload file: %s", str(e))
        return False

if __name__ == "__main__":
    success = upload_test_file()
    if not success:
        exit(1)
