
class User:
    def __init__(self,first_name,last_name):
        self.fn = first_name
        self.ln = last_name

    def describe_user(self):
        print(f"Username: {self.fn} {self.ln}")

    def grert_user(self):
        print(f"Thanks {self.fn} {self.ln} to join here!")

user = User('A R','Ashik')
user.describe_user()
user.grert_user()