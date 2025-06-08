import sys
from dbhelper import DBHelper

class Flipkart:
    def __init__(self):
        self.db = DBHelper()
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
              1. Enter 1 to register.
              2. Enter 2 to login.
              3. Anything else to leave.
            """)

            if user_input == "1":
                self.register()
            elif user_input == "2":
                self.login()
            else:
                print("Exiting...")
                sys.exit(1000)

    def register(self):
        name = input('Enter name : ')
        email = input('Enter email : ')
        password = input('Enter password : ')

        response = self.db.register(name,email,password)

        if response:
            print("Registration successful")
        else:
            print('Registration fails')
        self.menu()

    def login(self):
        email = input('Enter email : ')
        password = input('Enter password : ')

        data = self.db.search(email,password)

        if len(data) == 0:
            print('Incorrect email or password')
            self.login()
        else:
            print('Hello', data[0][1])


# Run the app
obj = Flipkart()
