import sqlite3


class User:
    def __init__(self, user_id, username, password):
        self.id = user_id,
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        select_query = "SELECT * FROM users WHERE username=?"

        result = cursor.execute(select_query, (username,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_user_id(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        select_query = "SELECT * FROM users WHERE id=?"

        result = cursor.execute(select_query, (username,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user
