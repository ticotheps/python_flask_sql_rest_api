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

# Runs the server
if __name__ == '__main__':
    app.run(debug=True)