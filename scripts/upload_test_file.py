import os
from modules.s3_connection import get_s3_client, check_bucket_exists
from dotenv import load_dotenv
from modules.logger import logger
import glob

# Load environment variables 
load_dotenv()

def upload_test_files():
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

    # Get all md files from test_files directory
    test_files = glob.glob("./test_files/*.md")
    if not test_files:
        logger.error("No markdown files found in ./test_files")
        return False

    success_count = 0
    for file_path in test_files:
        try:
            # Read file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Use filename as key in S3
            file_key = os.path.basename(file_path)
            
            logger.debug("Uploading file %s to %s/%s", file_path, bucket, file_key)
            s3_client.put_object(
                Bucket=bucket,
                Key=file_key,
                Body=content,
                ContentType='text/markdown'
            )
            logger.info("Successfully uploaded %s to %s/%s", file_path, bucket, file_key)
            success_count += 1
            
        except Exception as e:
            logger.error("Failed to upload file %s: %s", file_path, str(e))

    total_files = len(test_files)
    logger.info("Upload complete. Successfully uploaded %d/%d files", success_count, total_files)
    return success_count == total_files

if __name__ == "__main__":
    success = upload_test_files()
    if not success:
        exit(1)
