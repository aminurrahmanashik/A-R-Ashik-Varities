

def build_person(first_name,last_name):
    """Return a dictioanry of information abiut a person"""
    full_name = f"{first_name} {last_name}"
    return full_name



while True:
    print("Please tell me your name:")
    print("Enter 'q' to quit")
    first_name = input("First Name:")
    if first_name == 'q':
        break
    last_name = input("Last Name:")
    formatted_name = build_person(first_name,last_name)
    print(f"Hello {formatted_name.title()}!")