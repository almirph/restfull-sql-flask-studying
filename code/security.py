from werkzeug.security import safe_str_cmp
from user import User


def authenticate(username, password):
    user = User.find_by_username(username)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
