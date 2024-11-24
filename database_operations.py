import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

load_dotenv()

def create_reports_table():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    
    try:
        # Drop existing table if it exists
        cur.execute("DROP TABLE IF EXISTS reports CASCADE;")
        
        create_table_query = """
        CREATE TABLE reports (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            user_id VARCHAR(100) NOT NULL,
            username VARCHAR(100) NOT NULL,
            offence TEXT NOT NULL,
            action VARCHAR(255) NOT NULL,
            reported_by VARCHAR(100) DEFAULT NULL,
            advice TEXT DEFAULT NULL,
            note TEXT DEFAULT NULL,
            proof TEXT DEFAULT NULL,
            rm VARCHAR(255) DEFAULT NULL
        );
        """
        cur.execute(create_table_query)
        
        # Create indexes
        cur.execute("""
            CREATE INDEX idx_reports_timestamp ON reports(timestamp);
            CREATE INDEX idx_reports_username ON reports(username);
        """)
        
    finally:
        cur.close()
        conn.close()

def truncate_table():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    
    try:
        cur.execute("TRUNCATE TABLE reports;")
    finally:
        cur.close()
        conn.close()

def delete_reports_table():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    
    try:
        cur.execute("DROP TABLE IF EXISTS reports CASCADE;")
    finally:
        cur.close()
        conn.close()

def get_all_logs():
    engine = create_engine(os.getenv('DATABASE_URL'))
    try:
        df = pd.read_sql_query("""
            SELECT * FROM reports 
            ORDER BY timestamp DESC
        """, engine)
        return df
    finally:
        engine.dispose() 