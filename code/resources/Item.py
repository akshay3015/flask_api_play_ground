from flask_jwt import JWT, jwt_required
from flask_restful import Resource, reqparse
import sqlite3
import mysql.connector
from models.item_model import ItemModel
from flask import request
from db import db

# database = mysql.connector.connect(host='127.0.0.1', user='root', passwd='12345678', database='flask_db')


# handle addition/fetching  item
class Item(Resource):
    """docstring for ."""

    @jwt_required()
    def get(self, name):
        row = ItemModel.find_by_name(name)

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

        return {'msg': 'item not found'}, 404

    @jwt_required()
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('name',
                            type=str,
                            required=True,
                            help='this field can not be empty')

        parser.add_argument('price',
                            type=float,
                            required=True,
                            help='this field can not be empty')
        data = parser.parse_args()

        item = ItemModel(data['name'], data['price'])
        try:
            item.save_to_db()
        except:
            return {'msg': 'error occured while adding item  '}, 500

        return {'msg': 'item added successfully'}, 201

    # def post(self, name):
    #     data = request.get_json(silent=True)
    #     firstName = data['name']
    #
    #     lastName = data['password']
    #     cur = database.cursor()
    #     cur.execute("INSERT INTO user(username, password) VALUES (%s, %s)", (firstName, lastName))
    #     database.commit()
    #     cur.close()
    #     return {'message': 'user created successfully'}


# handling of multiple items
class ItemList(Resource):
    @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        rows = result.fetchall()

        cursor.close()
        if rows:
            return {'item': rows}

        return {'msg': 'items not found'}, 404
