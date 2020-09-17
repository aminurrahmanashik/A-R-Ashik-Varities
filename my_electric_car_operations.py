
from my_electric_car_classes import ElectricCar,Car

my_beetle = Car('volkwagen','beetle',2020)
print(my_beetle.get_descriptive_name())


my_tesla = ElectricCar('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_bettary()
my_tesla.battery.get_range()