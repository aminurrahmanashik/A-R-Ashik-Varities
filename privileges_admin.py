
import separate_user_module

"""separarte class"""
class Privileges:
    def __init__(self ,first ,last):
        self.fst = first
        self.lst = last
        self.privileges = ["can add post", "can delete post", "can ban user", "you can see post"]

    def show_privileges(self ,privilege_number):
        print(f"The administrator {self.fst.title()} {self.lst.title()} can {self.privileges[privilege_number]}")


"""child class"""
class Admin(separate_user_module.User):

    def __init__(self ,first ,last):
        super().__init__(first ,last)
        self.privileges = Privileges(first ,last)
