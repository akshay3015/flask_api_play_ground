from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

'''
JWT --> JSON Web Token 
for Obfuscation of data

'''

app = Flask(__name__)
app.secret_key = "secret"
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

items = []


# handle addition/fetching  item
class Item(Resource):
    """docstring for ."""

    @jwt_required()
    def get(self, name):
        # returns first item found by filter function
        item = next(filter(lambda x: x['name'] == name, items), None)  # None ---> default  val if no match found)
        return {'item': item}, 200 if item else 404  # 200 OK 404 not found

    @jwt_required()
    def post(self, name):
        '''
        request.get_json()
        will give an error is wrong playlaod is passed
        can be handled by request.get_json(force=True) but dangerous process the data even if incorrect
        request.get_json(silent=True) better does not give error just return null
        '''

        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An  item '{}' already exist".format(name)}, 200

        data = request.get_json(silent=True)
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201  # created


# handling of multiple items
class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {'items': items}, 200  # OK


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
