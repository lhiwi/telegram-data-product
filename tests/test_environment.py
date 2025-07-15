import os
from dotenv import load_dotenv
import telethon
import psycopg2

def test_dependencies_installed():
    try:
        from telethon import TelegramClient
        from sqlalchemy import create_engine
    except ImportError as e:
        assert False, f"Dependency missing: {e}"

def test_env_variables_loaded():
    load_dotenv()

    required_vars = [
        "TELEGRAM_API_ID",
        "TELEGRAM_API_HASH",
        "TELEGRAM_SESSION",
        "POSTGRES_USER",
        "POSTGRES_PASSWORD",
        "POSTGRES_DB",
        "POSTGRES_HOST",
        "POSTGRES_PORT"
    ]

    for var in required_vars:
        assert os.getenv(var), f"Missing environment variable: {var}"

def test_postgres_connection():
    load_dotenv()

    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT")
        )
        conn.close()
    except Exception as e:
        assert False, f"PostgreSQL connection failed: {e}"
