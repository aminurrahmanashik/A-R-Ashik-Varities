

def describe_pet(animal_type,pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('cat','mini')
describe_pet('dog','kalu')
describe_pet(animal_type='hamster', pet_name='harry')
"""we can change the argument explicitly using key-value pair with any order we want."""
describe_pet(pet_name='harry', animal_type='hamster')
