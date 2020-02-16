from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initializes the app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Configures SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializes Database
db = SQLAlchemy(app)

# Initializes Marshmallow (serializer + deserializer)
ma = Marshmallow(app)

# Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)
    
    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty
        
# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')
    
# Initializes Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True) 

# Handles POST requests to '/product' endpoint
@app.route('/product', methods=['POST'])
# Adds a product to the database
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    
    # Instantiates a new instance of a 'Product' object
    new_product = Product(name, description, price, qty)
    
    db.session.add(new_product)
    db.session.commit()
    
    return product_schema.jsonify(new_product)

# Handles GET requests to '/product' endpoint
@app.route('/product', methods=['GET'])
# Returns all products in the database
def get_products():
    # Utilizes ORM instead of raw SQL query "SELECT * FROM products" 
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

# Handles GET requests to '/product/<id>' endpoint
@app.route('/product/<id>', methods=['GET'])
# Returns a SINGLE PRODUCT from the database
def get_single_product(id):
    single_product = Product.query.get(id)
    return product_schema.jsonify(single_product)

# Runs the server
if __name__ == '__main__':
    app.run(debug=True)