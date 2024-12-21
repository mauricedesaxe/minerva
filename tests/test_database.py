import pytest
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from sqlalchemy.sql import text

from minerva.database import create_db_engine, get_db
from minerva.config import get_config

def test_create_db_engine():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get database URL from config
    config = get_config()
    expected_db_url = config.postgres_dsn
    
    # Create engine
    engine = create_db_engine()
    
    # Verify engine was created correctly
    assert isinstance(engine, Engine)
    
    # Compare URL components individually to avoid password masking issues
    engine_url = engine.url
    expected_parts = expected_db_url.split('@')
    credentials = expected_parts[0].split('//')[-1].split(':')[0]
    host_part = expected_parts[1]
    
    assert engine_url.username == credentials
    assert engine_url.host in host_part
    assert engine_url.database == 'postgres'

def test_get_db():
    # Load environment variables from .env file 
    load_dotenv()
    
    with get_db() as db:
        # Verify we get a valid session
        assert isinstance(db, Session)
        
        # Verify session is bound to our engine
        assert db.get_bind().url == create_db_engine().url
        
        # Execute a simple query to verify the connection is live
        result = db.execute(text("SELECT 1")).scalar()
        assert result == 1
        
        # Test transaction rollback works
        db.execute(text("CREATE TABLE IF NOT EXISTS test_table (id INTEGER)"))
        db.execute(text("INSERT INTO test_table (id) VALUES (1)"))
        db.rollback()
        
        # Verify the rollback worked (table should not exist)
        with pytest.raises(Exception):
            db.execute(text("SELECT * FROM test_table")).scalar()