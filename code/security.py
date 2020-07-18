from user import User
from werkzeug.security import safe_str_cmp

users = [

    User(1, 'user', '1234')

]

user_name_mapping = {
    u.username: u for u in users
}

user_id_mapping = {
    1: u for u in users
}


def authenticate(username, password):
    user = user_name_mapping.get(username, None)  # if no user found return None
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    print(payload)
    user_id = payload['identity'][0]
    print(user_id)
    return user_id_mapping.get(user_id, None)
