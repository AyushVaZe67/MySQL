import mysql.connector

class DBHelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='db-demo'
            )
            self.mycursor = self.conn.cursor()
        except:
            print('Error')
        else:
            print('Connected to Database')

    def register(self, name, email, password):
        try:
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            values = (name, email, password)
            self.mycursor.execute(query, values)
            self.conn.commit()
        except Exception as e:
            print("Error:", e)
            return -1
        else:
            return 1

    def search(self,email,password):
        self.mycursor.execute("""
            SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'
        """.format(email,password))
        data = self.mycursor.fetchall()
        return data