from car import Car

# class that doesn't inherit from any other class
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self,bz = 75):
        """Initialize the battery's attributes"""
        self.battery_size = bz

    def describe_bettary(self):
        """Print as statement describing the battery size"""
        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""

        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

"""CHILD CLASS"""
class ElectricCar(Car):
    """Represent aspects of a car,specific to electric vehicles"""
    # super->parent class & sub->child class
    def __init__(self,e_make,e_model,e_year):
        """Initialize  attributes of the parent class."""
        # this super function allows to call a method from a parent class
        super().__init__(e_make,e_model,e_year)

        # this will create a new instance of Battery
        # with a default value 75 as we are not specifying the value of size
        """ If u want to pass any value through this instance, we can"""
        self.battery = Battery()
        # Defining Attribute for the Child Class
        # self.battery_size = 75

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank!")


"""
p_tesla = Car('corolla','X',2019)
my_tesla = ElectricCar('tesla','model s',2019)
your_tesla = ElectricCar('corolla','X',2019)
print(my_tesla.get_descriptive())
# to call ordinary classes,we need to use 2 dots
my_tesla.battery.describe_bettary()
your_tesla.battery.describe_bettary()
my_tesla.fill_gas_tank()
p_tesla.fill_gas_tank()
my_tesla.battery.get_range()
"""
