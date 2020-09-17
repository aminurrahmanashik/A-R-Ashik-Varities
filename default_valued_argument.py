
print("Two arguments by default")
def describe_pet(animal_type='cat',pet_name='mini'):
    """Display information about a pet"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()


print("\nOnly one argument by default")
# there can be any order of the parameters as we direclty assigned the animal's name
def describe_pet(animal_type,pet_name='mini'):
    """Display information about a pet"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='cat')

print("\nBut if we try for the sigle argument which is coming from the caller,then-",
      "\nThis parameter must be at the first place of all other arguments")
def describe_pet(animal_type,pet_name='mini'):
    """Display information about a pet"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('cat')
