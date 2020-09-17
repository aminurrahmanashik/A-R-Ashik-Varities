
from pizzas import make_pizza
def cars(car_name,car_catagory,**others):
    others['Car'] = car_name
    others['Car type'] = car_catagory
    return others

car = cars('toyota','X-corolla',price = '$3000',color  = 'blue',location = 'dhaka')
print(car)
