import os
from s3_connection import get_s3_client, check_bucket_exists
from dotenv import load_dotenv

# Load environment variables 
load_dotenv()

def upload_test_file():
    # Get bucket name from env
    bucket = os.getenv('BUCKET_NAME')
    if not bucket:
        print("Error: BUCKET_NAME environment variable not set")
        return False

    # Check bucket exists
    s3_client = get_s3_client()
    if not check_bucket_exists(bucket, s3_client):
        print(f"Error: Bucket '{bucket}' not found or not accessible")
        print("Check your credentials and bucket name")
        return False

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
        s3_client.put_object(
            Bucket=bucket,
            Key=file_key,
            Body=test_content,
            ContentType='text/markdown'
        )
        print(f"Successfully uploaded test file to {bucket}/{file_key}")
        return True
    except Exception as e:
        print(f"Error uploading file: {str(e)}")
        return False

if __name__ == "__main__":
    upload_test_file()
