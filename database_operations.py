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

def get_paginated_logs(page=1, per_page=10, search=''):
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    try:
        cur = conn.cursor()
        
        # Get total records with search
        if search:
            search_pattern = f'%{search}%'
            cur.execute("""
                SELECT COUNT(*) FROM reports 
                WHERE username ILIKE %s 
                OR user_id ILIKE %s 
                OR offence ILIKE %s
                OR action ILIKE %s
                OR reported_by ILIKE %s
                OR advice ILIKE %s
                OR note ILIKE %s
                OR proof ILIKE %s
                OR rm ILIKE %s
            """, (search_pattern,) * 9)
        else:
            cur.execute("SELECT COUNT(*) FROM reports")
        
        total_records = cur.fetchone()[0]
        
        # Get paginated records
        offset = (page - 1) * per_page
        if search:
            search_pattern = f'%{search}%'
            cur.execute("""
                SELECT * FROM reports 
                WHERE username ILIKE %s 
                OR user_id ILIKE %s 
                OR offence ILIKE %s
                OR action ILIKE %s
                OR reported_by ILIKE %s
                OR advice ILIKE %s
                OR note ILIKE %s
                OR proof ILIKE %s
                OR rm ILIKE %s
                ORDER BY timestamp DESC 
                LIMIT %s OFFSET %s
            """, (search_pattern,) * 9 + (per_page, offset))
        else:
            cur.execute("""
                SELECT * FROM reports 
                ORDER BY timestamp DESC 
                LIMIT %s OFFSET %s
            """, (per_page, offset))
        
        columns = [desc[0] for desc in cur.description]
        records = [dict(zip(columns, record)) for record in cur.fetchall()]
        
        return total_records, records
    finally:
        conn.close() 