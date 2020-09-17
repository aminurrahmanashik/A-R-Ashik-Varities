

"""PARENT CLASS"""
class Car:
    """A simple attempt to represent a car"""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    # method that modifies the odometer
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value
        Reject the change if it attempts to roll te odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    # method that increments the odometer
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Check whether your car is filled with gas!")


    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")


# class that doesn't inherit from any other class
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self,bs=75):
        """Initialize the battery's attributes"""
        self.battery_size = bs

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

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100



"""CHILD CLASS"""
class ElectricCar(Car):
    """Represent aspects of a car,specific to electric vehicles"""
    # super->parent class & sub->child class
    def __init__(self,e_make,e_model,e_year):
        """Initialize  attributes of the parent class."""
        # this super function allows to call a method from a parent class
        super().__init__(e_make,e_model,e_year)
        self.battery_size = 75
        # this will create a new instance of Battery
        # with a default value 75 as we are not specifying the value of size
        """ If u want to pass any value through this instance, we can"""
        self.battery = Battery()
        # Defining Attribute for the Child Class
        # self.battery_size = 75

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla','model s',2019)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
