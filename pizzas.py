
# using *to take as many arguments as you can
def make_pizza(*toppings):
    """Print the list of toppingd that have been requested."""
    print("\nLooping through this tuple")
    print(toppings)

#make_pizza('pepperoni')
#make_pizza('mushrooms','green peppers','extra cheese')


print("\nNow looping through the tuple.")
def make_pz(*toppings):
    """Summerize the pizza we  are about to make"""
    print("\nMaking a pizza with the following toppings:")

    for topping in toppings:
        print(f"-{topping}")

#make_pz('mushrooms','green peppers','extra cheese')