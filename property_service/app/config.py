import os

DATABASE_CONFIG = {
    'host': os.getenv('DATABASE_HOST', 'localhost'),
    'port': os.getenv('DATABASE_PORT', 3306),
    'user': os.getenv('DATABASE_USER', 'root'),
    'password': os.getenv('DATABASE_PASSWORD', ''),
    'database': os.getenv('DATABASE_NAME', 'habi_db'),
}

