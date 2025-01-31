import sqlite3
from datetime import datetime

class Model:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')  
        self.cursor = self.conn.cursor()

    def add_mat(self, name_mat, name_com, type_mat, count, expiry, Suitable_age):
        self.cursor.execute("INSERT INTO mat (name_mat, name_com, type_mat, count, expiry, Suitable_age) VALUES (?, ?, ?, ?, ?, ?)", (name_mat, name_com, type_mat, count, expiry, Suitable_age))
        self.conn.commit()


        
    def get_mat(self):
        self.cursor.execute('SELECT * FROM mat')
        rows = self.cursor.fetchall()  # جلب جميع البيانات دفعة واحدة
        mat_id = [col[0] for col in rows] 
        name_mat = [col[1] for col in rows] 
        name_com = [col[2] for col in rows]
        type_mat = [col[3] for col in rows] 
        count = [col[4] for col in rows]
        expiry = [col[5] for col in rows]
        Suitable_age = [col[6] for col in rows]
        return name_mat, name_com, type_mat, count, expiry, Suitable_age
    
    
    def del_mat(self, mat_id):
        self.cursor.execute("DELETE FROM mat WHERE id = ?", (mat_id,))
        self.conn.commit()  

    
    def update_mat(self, mat_id, ame_mat, name_com, type_mat, count, expiry, Suitable_age):
        self.cursor.execute('''
            UPDATE Materials
            SET name_of_material = ?, type_of_materials = ?, expaier = ?, price = ?
            WHERE id = ?
        ''', (ame_mat, name_com, type_mat, count, expiry, Suitable_age, mat_id))
        self.conn.commit()

        





        
#######################################################دفع مؤجل 
   
    def add_deferred(self, cos_name, cos_phone, cos_location , price):
        self.cursor.execute("INSERT INTO deferred ( cos_name, cos_phone, cos_location , price) VALUES (?, ?, ?, ?)", ( cos_name, cos_phone, cos_location , price))
        self.conn.commit()





    def get_deferred(self):
        self.cursor.execute('SELECT * FROM deferred')
        rows = self.cursor.fetchall()  
        defe_id = [col[0] for col in rows] 
        cos_name = [col[1] for col in rows] 
        cos_phone = [str(col[2]) for col in rows]  
        cos_location = [col[3] for col in rows] 
        price = [col[4] for col in rows]
        return defe_id, cos_name, cos_phone, cos_location , price
    
    

    

    
    def del_deferred(self, deferred_id):
        self.cursor.execute("DELETE FROM deferred WHERE id = ?", (deferred_id,))
        self.conn.commit()


    
    def update_deferred(self, deferred_id, cos_name, cos_phone, cos_location , price):
        self.cursor.execute('''
            UPDATE deferred
            SET cos_name = ?,  cos_phone = ?, cos_location = ?, price = ?
            WHERE id = ?
        ''', (cos_name, cos_phone, cos_location , price, deferred_id))
        self.conn.commit()    
             
        