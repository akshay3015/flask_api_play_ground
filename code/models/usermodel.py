import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(70))
    password = db.Column(db.String(70))

    def __init__(self, user_id, username, password):
        self.id = user_id,  # must match with column name
        self.username = username  # must match with column name
        self.password = password  # must match with column name

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
