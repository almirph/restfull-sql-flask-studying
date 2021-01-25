from flask_jwt import JWT, jwt_required
from model.ItemModel import ItemModel
from flask_restful import Resource, reqparse


class ItemResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="Esse campo não pode ser branco"
                        )

    # @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        data = ItemResource.parser.parse_args()
        item = ItemModel(name, data['price'])
        item.save_to_db()
        return {'item': item.json()}, 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'item removido'}

    def put(self, name):
        data = ItemResource.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            return {'message': f'Item com nome {name} não existe'}, 404
        item.price = data['price']
        item.save_to_db()
        return {'item': item.json()}, 201


class ItemsResource(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}, 200
