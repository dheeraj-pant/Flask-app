import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import Itemmodel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    
    @jwt_required()
    def get(self,name):
        item=Itemmodel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'item not found'},404    


    def post(self,name):
        if Itemmodel.find_by_name(name):
            return {'message': 'An item with name {name} is already exist'},400

        data=Item.parser.parse_args()
        item=Itemmodel(name,data['price'])
        try:
            item.insert()
        except:
            return {'message': 'AN error occured while insertion'},500    

        return item.json(),201

    def delete(self,name):
        item=Itemmodel.find_by_name(name)
        if item is None:
            return {'message':'item not found'},404
       
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query='delete from items where name=?'
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()    
        return{'message':'item deleted sucessfully'},200

    def put(self, name):
        data = Item.parser.parse_args()
        # Once again, print something not in the args to verify everything works
        item = Itemmodel.find_by_name(name)
        updated_item=Itemmodel(name,data['price'])
        if item is None:
            try:
                updated_item.insert()
            except:
                return {'message': 'AN error occured while insertion'},500
 
        else:
            try:
                updated_item.update() 
            except:
                return {'message': 'AN error occured while insertion'},500
            
        return updated_item.json()    

class Itemlist(Resource):
    def get(self):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query='select * from items'
        items=[]
        result=cursor.execute(query)
        for row in result:
            items.append(row)
        connection.close()    
        return {'item': items},200