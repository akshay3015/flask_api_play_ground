from flask import Flask, jsonify

'''__name__  special python variable 
that gives each unique name'''

app = Flask(__name__)

stores = [
    {
        'name': 'Store one',
        'items': [
            {
                'name': 'Oreo',
                'price': '0.99'
            }
        ]
    }
]


# POST to receive data
# GET to send data back only


@app.route('/')  # home page
def home():
    return "Hello World, Bambi here!!"


# POST /store data {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item {name:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass


app.run(port=5000)
