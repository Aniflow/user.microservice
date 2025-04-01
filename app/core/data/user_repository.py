from typing import Dict

from mysql.connector import Error

from .database import db


class UserRepository:
    """Handles database operations related to users."""

    @staticmethod
    def get_user_by_id(user_id: int) -> Dict:
        """Fetch user by ID from the database."""
        connection = db.get_connection()
        if not connection:
            print("Error: No database connection.")
            return {}

        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT * FROM users WHERE id = %s",
                (user_id,)
            )
            result = cursor.fetchone()
            if result:
                return result
            else:
                print(f"User with ID {user_id} not found.")
                return {}
        except Error as e:
            print(f"Error executing query: {e}")
            return {}
        finally:
            try:
                cursor.close()
            except Error as e:
                print(f"Error closing cursor: {e}")
            try:
                connection.close()
            except Error as e:
                print(f"Error closing connection: {e}")
