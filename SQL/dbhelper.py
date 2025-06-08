import mysql.connector

class DBHelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='db-demo')
            self.mycursor = self.conn.cursor()
        except:
            print('Error')
        else:
            print('Connected to Database')