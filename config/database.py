from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv(".env")

# Database Configuration
connection = mysql.connector.connect(
    host=os.getenv('DATABASE_HOST'),
    user=os.getenv('DATABASE_USERNAME'),
    password=os.getenv('DATABASE_PASSWORD'),
    database=os.getenv('DATABASE'),
    autocommit=True,
    # ssl_mode="VERIFY_IDENTITY",
    # ssl={"ca": "/etc/ssl/cert.pem"}
)