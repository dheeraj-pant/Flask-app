import sqlite3

class Itemmodel():
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def json(self):
        return {'name':self.name,'price':self.price}   

    @classmethod
    def find_by_name(cls,name):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        query='select * from items where name=?'
        item=cursor.execute(query,(name,)).fetchone()
        connection.close()
        if item:
            return cls(*item) 
       
    def insert(self):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query='insert into items values(?,?)'
        cursor.execute(query,(self.name,self.price))
        connection.commit()
        connection.close()

    def update(self):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query='update items set price=? where name=?'
        cursor.execute(query,(self.price,self.name))
        connection.commit()
        connection.close()     