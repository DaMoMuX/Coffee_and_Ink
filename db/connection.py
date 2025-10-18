import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    try:
        connection = psycopg2.connect(
            dbname = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            host = os.getenv("DB_HOST"),
            port = os.getenv("BD_PORT")
        )
        return connection
    except Exception as e:
        print("Error while connecting whit database")
        return None
    
def test_connection():
    
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            print("Connected to:", version)
        except Exception as e:
            print("Error while executing:", e)
        finally:
            cursor.close()
            conn.close()
            print("Connection closed.")
    else:
        print("No possible to stablish connection")
