
class Car:
    """A simple attempt to represent a car"""

    def __init__(self,make,model,year):
        """Inbitialize atteributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    # method that modifies the odometer
    def update_odometer(self,mileage):
        """Set the odometer reading to the given value
        Reject the change if it attempts to roll te odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # method that increments the odometer
    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


    def read_odometer(self):
        """Print a statement showing the car's milage"""
        print(f"This car has {self.odometer_reading} miles on it.")


# I've used this comment to make this class Car workable for another file my_car,py
"""
my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive())
# Modifying an Attribute’s Value Directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# Modifying an Attribute’s Value Through a Method
my_new_car.update_odometer(12)
my_new_car.read_odometer()
# Incrementing an Attribute’s Value Through a Method
my_new_car.increment_odometer(23_500)
my_new_car.read_odometer()

print("\nA new car entry.")
my_used_car = Car('subaru','outback',2015)
print(my_used_car.get_descriptive())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

"""