
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"The name of the restaurant is:{self.restaurant_name}")
        print(f"{self.restaurant_name}'s cuisine type is: {self.cuisine_type}")

    def open_resturant(self):
        print(f"{self.restaurant_name} is open!")

restaurant = Restaurant('Saladia','Owesome')
print(f"Restaurant: {restaurant.restaurant_name}\nCuisine Type: {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_resturant()

