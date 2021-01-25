import sqlite3
from flask_restful import Resource, reqparse
from model.UserModel import UserModel


class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="O campo não pode ser vazio"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="O campo não pode ser vazio"
                        )

    def post(self):
        data = UserResource.parser.parse_args()

        if(UserModel.find_by_username(data['username'])):
            return {"message": "usuário já existe"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201
