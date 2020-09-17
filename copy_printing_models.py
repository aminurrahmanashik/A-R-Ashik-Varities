

"""Here we'll show how to pass copied list(without modifying the original) as argument"""

# start with some designs that need to be printed.
def print_models(unprinted_designs,completed_models):
# Simulate peinting each design,until none are left.
# move each design to complete_models after printing.

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        print(f"List: {unprinted_designs}")


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model.title())

unprinted_designs = ['phone case','robot pendant','dodechahedron']
completed_models = []

print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)

# look here the 'unprinted_designs' is as it is!
print(unprinted_designs)