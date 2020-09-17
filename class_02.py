
class Meal:
    def __init__(self,type,objective):
        self.type = type
        self.objective = objective


    def greet(self):
        print(f"Bro {self.type} is ready for you!")

    def choosing(self):
        print(f"You have choosen {self.objective} type {self.type}")


my_meal1 = Meal('soup','chicken')
my_meal2 = Meal('burger','beef')
my_meal1.greet()
my_meal1.choosing()
#print(f"Bro {my_meal1.type} is ready for you!")
#print(f"You have choose {my_meal1.objective} type {my_meal1.type}")
print(f"Bro {my_meal2.type} is ready for you!")
print(f"You have choosen {my_meal2.objective} type {my_meal2.type}")
