import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-E-commerce-key")
    
    oracle_db = "oracle+oracledb://SALE:123@localhost:1521/?service_name=ORCL"
    os_dir = os.environ.get("DATABASE_URL")
    
    SQLALCHEMY_DATABASE_URI = (os_dir or oracle_db)

    SQLALCHEMY_TRACK_MODIFICATIONS = False