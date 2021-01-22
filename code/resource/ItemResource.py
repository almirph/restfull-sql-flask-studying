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
        item.insert_self()
        return {'item': item.json()}, 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item == None:
            return {'message': f'Item com o nome {name} não foi encontrado.'}, 404
        item.delete_self()
        return {'message': 'Item Deleted'}, 200

    def put(self, name):
        data = ItemResource.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item == None:
            return {'message': f'Item com nome {name} não existe'}, 404
        item.update_self(data['price'])
        return {'item': item.json()}, 201


class ItemsResource(Resource):
    def get(self):
        items = ItemModel.find_all_dict()
        return {'items': items}, 200
