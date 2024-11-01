
import mysql.connector

class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student_management"
        )
        self.mycursor = self.mydb.cursor()
obj = Database()

















