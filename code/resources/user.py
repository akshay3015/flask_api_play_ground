import sqlite3
from flask_restful import Resource, reqparse
from models.usermodel import UserModel


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
        if UserModel.find_by_username(username=usrname):
            return {'msg': 'user already exists'}, 400
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL,?,?)"
        cursor.execute(query, (usrname, password))
        connection.commit()
        connection.close()
        return {'msg': 'user created successfully'}, 201
