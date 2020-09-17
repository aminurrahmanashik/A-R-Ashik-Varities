
# method is a special type of function that is defined inside the class
# we can write capital dog as well, but just for visualization, we left it titled
class Dog:
    """A simple attempt to model a dog"""

    # method-01
    def __init__(self,name,age):
        """Initialize  name and age attributes"""
        # we can also use another variable to be names as 'name' at left side of it
        self.n = name
        self.a = age
    # method-02
    # protiti method er sathei self pass kora hoyeche jate each object can have access these methods
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.n} is now sitting.")
    # method-03
    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.n} aged {self.a} is rolled over.")

my_dog = Dog('Kalu',6)
# if we pass the attribute name, it will only work for the last updated one
# here, my_dog will work for the Dog('Tiger',20) only
my_dog = Dog('Tiger',20)
your_dog = Dog('Lalu',10)
print(f"My dog's name is {my_dog.n}")
print(f"My dog is {my_dog.a} years old.")
my_dog.sit()
my_dog.roll_over()
print(f"My dog's name is {your_dog.n}")
print(f"My dog is {your_dog.a} years old.")
your_dog.sit()
your_dog.roll_over()
