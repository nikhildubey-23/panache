import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')

def get_connection():
    if not DATABASE_URL:
        raise Exception("DATABASE_URL not found in environment variables")
    return psycopg2.connect(DATABASE_URL, sslmode='require')

def query(sql, params=None, fetch=True):
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(sql, params)
            if fetch and cur.description:
                result = cur.fetchall()
                return result
            conn.commit()
            return None
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def db_available():
    return DATABASE_URL is not None

def init_tables():
    if not db_available():
        print("No DATABASE_URL set - skipping table creation")
        return
    statements = [
        """
        CREATE TABLE IF NOT EXISTS admin_users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT NOW()
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS bookings (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL,
            email VARCHAR(255),
            appointment_date DATE NOT NULL,
            appointment_time VARCHAR(20) NOT NULL,
            consultation_type VARCHAR(100) NOT NULL,
            message TEXT,
            status VARCHAR(20) DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT NOW()
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS contact_messages (
            id SERIAL PRIMARY KEY,
            name VARCHAR(200) NOT NULL,
            email VARCHAR(255) NOT NULL,
            phone VARCHAR(20),
            subject VARCHAR(255),
            message TEXT NOT NULL,
            status VARCHAR(20) DEFAULT 'unread',
            created_at TIMESTAMP DEFAULT NOW()
        )
        """
    ]
    for stmt in statements:
        query(stmt, fetch=False)

def seed_admin():
    if not db_available():
        return
    from werkzeug.security import generate_password_hash
    existing = query("SELECT id FROM admin_users WHERE username = 'admin'")
    if not existing:
        pw_hash = generate_password_hash('admin123')
        query(
            "INSERT INTO admin_users (username, password_hash) VALUES (%s, %s)",
            ('admin', pw_hash),
            fetch=False
        )
        print("Default admin created: username=admin, password=admin123")
