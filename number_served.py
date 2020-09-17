
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant is:{self.restaurant_name}")
        print(f"{self.restaurant_name}'s cuisine type is: {self.cuisine_type}")

    def open_resturant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self,set_number):
        self.number_served = set_number
        print(f"You set the restaurant to serve {self.number_served} peoples.")

    def increment_number_served(self,increment_number):
        self.number_served += increment_number
        print(f"Serving capacity increased to {self.number_served} peoples.")

restaurant = Restaurant('Final Tune','Hygenic')
print(f"The restaurant {restaurant.restaurant_name} provides service to {restaurant.number_served} peoples")
restaurant.set_number_served(16)
restaurant.increment_number_served(5)
