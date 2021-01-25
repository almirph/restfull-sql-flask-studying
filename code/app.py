import sqlite3
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from security import authenticate, identity
from resource.UserResource import UserResource
from resource.ItemResource import ItemResource, ItemsResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(ItemResource, '/item/<string:name>')
api.add_resource(ItemsResource, '/items')
api.add_resource(UserResource, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
