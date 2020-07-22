import sqlite3
from flask_restful import Resource, reqparse


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


class RegisterUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field can not be empty'
                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field can not be empty'
                        )

    def post(self):
        data = RegisterUser.parser.parse_args()
        usrname = data['username']
        password = data['password']
        if User.find_by_username(username=usrname):
            return {'msg': 'user already exists'}, 400
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL,?,?)"
        cursor.execute(query, (usrname, password))
        connection.commit()
        connection.close()
        return {'msg': 'user created successfully'}, 201
