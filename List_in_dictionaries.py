
# store information about a pizza being ordered
print("store information about a pizza being ordered")
pizza =  {
	'crust' : 'thick',
	'toppings' : ['mashrooms','extra cheese']
}

print("\nSummerizing the order.")

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
	print("\t" +  topping)