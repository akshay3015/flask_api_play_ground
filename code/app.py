from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import RegisterUser
from resources.Item import Item, ItemList

'''
JWT --> JSON Web Token 
for Obfuscation of data

'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////code/data.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # turn off Flask SQLAlchemy tracker
app.secret_key = "secret"
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(RegisterUser, '/register')

'''
does not execute code on import only when the file is executed 
'''
if __name__ == '__main__':
    from db import db

    db.init_app(app)

    app.run(port=5000, debug=True)
