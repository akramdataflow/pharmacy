import sqlite3
from datetime import datetime

class Model:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')  
        self.cursor = self.conn.cursor()

    def add_mat(self, name_mat, name_com, type_mat, count, expiry, Suitable_age):
        self.cursor.execute("INSERT INTO mat (name_mat, name_com, type_mat, count, expiry, Suitable_age) VALUES (?, ?, ?, ?, ?, ?)", (name_mat, name_com, type_mat, count, expiry, Suitable_age))
        self.conn.commit()