import sqlite3

class Usermodel():
    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password

    @classmethod
    def find_by_user_name(cls,username):
        connection=sqlite3.connect('data.db')
        cursor =connection.cursor()

        select_query='select * from users where username=?'
        row=cursor.execute(select_query,(username,)).fetchone() 
        connection.close()
        if row:
            return cls(*row)

    @classmethod
    def find_by_user_id(cls,_id):
        connection=sqlite3.connect('data.db')
        cursor =connection.cursor()

        select_query='select * from users where id=?'
        row=cursor.execute(select_query,(_id,)).fetchone()
        if row:
            user= cls(*row)
        else:
            user= None    
        
        connection.close()
        return user  