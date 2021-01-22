import sqlite3
import json
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT

from security import authenticate, identity
from resource.UserResource import UserResource
from resource.ItemResource import ItemResource, ItemsResource

app = Flask(__name__)
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(ItemResource, '/item/<string:name>')
api.add_resource(ItemsResource, '/items')
api.add_resource(UserResource, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
