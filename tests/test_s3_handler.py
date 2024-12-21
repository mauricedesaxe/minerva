import pytest
from datetime import datetime
from botocore.exceptions import ClientError
from unittest.mock import MagicMock, patch

from minerva.s3.handler import S3Handler
from minerva.s3.types import S3File

@pytest.fixture
def mock_s3_response():
    return {
        'Body': MagicMock(read=lambda: b'test content'),
        'ContentType': 'text/plain',
        'ContentLength': 12,
        'LastModified': datetime.now(),
        'Metadata': {'test-key': 'test-value'},
        'ETag': '"abc123"',
        'VersionId': 'v1'
    }

@pytest.fixture
def s3_handler():
    with patch('boto3.client') as mock_boto3:
        handler = S3Handler()
        handler.s3 = mock_boto3.return_value
        yield handler

def test_get_file_success(s3_handler, mock_s3_response):
    # Setup
    s3_handler.s3.get_object.return_value = mock_s3_response
    
    # Execute
    result = s3_handler.get_file('test-bucket', 'test-key.txt')
    
    # Verify
    assert isinstance(result, S3File)
    assert result.bytes == b'test content'
    assert result.content_type == 'text/plain'
    assert result.size == 12
    assert result.metadata == {'test-key': 'test-value'}
    assert result.etag == 'abc123'
    assert result.version_id == 'v1'
    
    # Verify S3 client called correctly
    s3_handler.s3.get_object.assert_called_once_with(
        Bucket='test-bucket',
        Key='test-key.txt'
    )

def test_get_file_not_found(s3_handler):
    # Setup
    error_response = {'Error': {'Code': '404', 'Message': 'Not Found'}}
    s3_handler.s3.get_object.side_effect = ClientError(error_response, 'GetObject')
    
    # Execute and verify
    with pytest.raises(ClientError):
        s3_handler.get_file('test-bucket', 'nonexistent.txt') 

def test_get_file_with_no_metadata(s3_handler):
    # Setup response without optional fields
    minimal_response = {
        'Body': MagicMock(read=lambda: b'test content'),
        'ContentLength': 12,
        'LastModified': datetime.now(),
    }
    s3_handler.s3.get_object.return_value = minimal_response
    
    # Execute
    result = s3_handler.get_file('test-bucket', 'test-key.txt')
    
    # Verify defaults are used
    assert result.content_type == 'application/octet-stream'
    assert result.metadata == {}
    assert result.etag == ''
    assert result.version_id is None

def test_get_file_connection_error(s3_handler):
    # Setup connection error
    s3_handler.s3.get_object.side_effect = ClientError(
        {'Error': {'Code': 'ConnectionError', 'Message': 'Failed to connect'}},
        'GetObject'
    )
    
    # Execute and verify
    with pytest.raises(ClientError) as exc_info:
        s3_handler.get_file('test-bucket', 'test.txt')
    assert exc_info.value.response['Error']['Code'] == 'ConnectionError'

def test_get_file_permission_denied(s3_handler):
    # Setup permission error
    s3_handler.s3.get_object.side_effect = ClientError(
        {'Error': {'Code': 'AccessDenied', 'Message': 'Access Denied'}},
        'GetObject'
    )
    
    # Execute and verify
    with pytest.raises(ClientError) as exc_info:
        s3_handler.get_file('test-bucket', 'test.txt')
    assert exc_info.value.response['Error']['Code'] == 'AccessDenied'

def test_get_file_large_file(s3_handler):
    # Setup large file response (10MB)
    large_content = b'x' * (10 * 1024 * 1024)  # 10MB of data
    large_response = {
        'Body': MagicMock(read=lambda: large_content),
        'ContentType': 'application/pdf',
        'ContentLength': len(large_content),
        'LastModified': datetime.now(),
        'Metadata': {},
        'ETag': '"large123"',
    }
    s3_handler.s3.get_object.return_value = large_response
    
    # Execute
    result = s3_handler.get_file('test-bucket', 'large.pdf')
    
    # Verify
    assert len(result.bytes) == 10 * 1024 * 1024
    assert result.content_type == 'application/pdf'
    assert result.size == len(large_content)

def test_get_file_with_special_characters(s3_handler, mock_s3_response):
    # Test with special characters in key
    s3_handler.s3.get_object.return_value = mock_s3_response
    special_key = 'folder/subfolder/file with spaces & special chars #1.txt'
    
    # Execute
    result = s3_handler.get_file('test-bucket', special_key)
    
    # Verify S3 client called correctly with special characters
    s3_handler.s3.get_object.assert_called_once_with(
        Bucket='test-bucket',
        Key=special_key
    )