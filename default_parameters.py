

print("\nif we explicitly assign the argumnets' value,then-",
      "\nNothing to worry about,as the assigned value will be worked for the function inside")
def describe_pet(animal_type,pet_name='mini'):
    """Display information about a pet"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# the values are going from the arguments will be worked, not the parameters by default one
describe_pet(animal_type='tiger',pet_name='badshah')
describe_pet('cat')


# we can do any type of keyword arguments/positional parameters/just value
def describe_pet(pet_name,animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('Willie')
describe_pet(pet_name='Willie')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')

