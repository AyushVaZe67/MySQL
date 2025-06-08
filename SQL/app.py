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
        print("Registration logic goes here.")

    def login(self):
        print("Login logic goes here.")

# Run the app
Flipkart()
