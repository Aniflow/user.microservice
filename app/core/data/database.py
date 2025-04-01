import os
from typing import Optional

from mysql.connector import pooling, Error
from dotenv import load_dotenv

load_dotenv()


class Database:
    """Manages a MySQL connection pool."""

    def __init__(self):
        self.pool = None
        self.init_pool()

    def init_pool(self):
        """Initialize the connection pool."""
        try:
            self.pool = pooling.MySQLConnectionPool(
                pool_name="user_pool",
                pool_size=int(os.getenv("DB_POOL_SIZE", 5)),
                host=os.getenv("DB_HOST", "localhost"),
                user=os.getenv("DB_USER"),  # Must set via .env
                password=os.getenv("DB_PASSWORD"),  # Must set via .env
                database=os.getenv("DB_NAME", "user_service_db"),
                port=int(os.getenv("DB_PORT", "3306")),
            )
        except Error as e:
            print(f"Database pool initialization error: {e}")

    def get_connection(self) -> Optional[pooling.PooledMySQLConnection]:
        """Get a connection from the pool."""
        try:
            return self.pool.get_connection()
        except Error as e:
            print(f"Error getting connection from pool: {e}")
            return None


db = Database()
