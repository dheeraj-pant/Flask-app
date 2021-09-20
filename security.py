from models.user import Usermodel

def authenticate(username,password):
    user= Usermodel.find_by_user_name(username)
    if user and user.password==password:
        return user

def identity(payload):
    user_id = payload['identity']
    return Usermodel.find_by_user_id(user_id)
