

"""parent class"""
class User:
    def __init__(self ,first_name ,last_name):
        self.fn = first_name
        self.ln = last_name

    def describe_user(self):
        print(f"Username: {self.fn.title()} {self.ln.title()}")

    def grert_user(self):
        print(f"Thanks {self.fn.title()} {self.ln.title()} to join here!")

