
"""parent class"""
class User:
    def __init__(self ,first_name ,last_name):
        self.fn = first_name
        self.ln = last_name

    def describe_user(self):
        print(f"Username: {self.fn.title()} {self.ln.title()}")

    def grert_user(self):
        print(f"Thanks {self.fn.title()} {self.ln.title()} to join here!")


"""separarte class"""
class Privileges:
    def __init__(self ,first ,last):
        self.fst = first
        self.lst = last
        self.privileges = ["can add post", "can delete post", "can ban user", "you can see post"]

    def show_privileges(self ,privilege_number):
        print(f"The administrator {self.fst.title()} {self.lst.title()} can {self.privileges[privilege_number]}")


"""child class"""
class Admin(User):

    def __init__(self ,first ,last):
        super().__init__(first ,last)
        self.privileges = Privileges(first ,last)

"""
admin = Admin('aminur rahman','ashik')
admin.describe_user()
admin.privileges.show_privileges(2)
admin = Admin('yeasin rahman','abir')
admin.describe_user()
admin.privileges.show_privileges(1)
"""







