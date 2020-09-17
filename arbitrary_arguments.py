
print("Mixing positional and Arbitrary arguments.")
# we need to add the arbitrary argument at the end of the function definition(parameter)
def make_pizza(size,*toppings):
    """Summerize the pizza we  are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")

    for topping in toppings:
        print(topping)

make_pizza(16,'pepperoni')
make_pizza(10,14,45)
make_pizza(45,'cucumber','ginger','cabbage','sugar')
make_pizza('cucumber',21,'ginger','cabbage','sugar')
