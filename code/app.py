from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

items = []


class Item(Resource):
    """docstring for ."""

    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item, 200  # OK
        return {'item': None}, 404  # not found

    def post(self, name):
        item = {'name': name, 'price': 12.90}
        items.append(item)
        return item, 201  # created


api.add_resource(Item, '/item/<string:name>')

app.run(port=5000, debug=True)
