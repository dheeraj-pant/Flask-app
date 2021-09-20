import sqlite3
from flask_restful import Resource,reqparse  
from models.user import Usermodel

class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='this field cannot be blank')
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='this field cannot be blank')

    def post(self):
        data=UserRegister.parser.parse_args()

        connection=sqlite3.connect('data.db')
        cursor =connection.cursor()

        if Usermodel.find_by_user_name(data['username']):
            return {'message' : 'user already exist'},400

        query="Insert into users values(null,?,?)"
        cursor.execute(query,(data['username'],data['password']))

        connection.commit()
        connection.close()

        return {'message':'user successfully created'},201


    
    

        