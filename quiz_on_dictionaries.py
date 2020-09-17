
# quiz-01
def email_list(domains):
	emails = []
	for users in domains.keys():
	  for user in domains[users]:
	    emails.append("{}@{}".format(user ,users))
	return(emails)

print(email_list
    ({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

# quiz-02
def groups_per_user(group_dictionary):
    user_groups = {}
    for dictionary in group_dictionary.keys():
        for users in group_dictionary[dictionary]:
            if users not in user_groups:
                user_groups[users] = []
            user_groups[users].append(dictionary)
    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

# quiz-03
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wrd_update = wardrobe.update(new_items)
print(wardrobe)


# quiz-05
def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for value in basket.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += value
	# Limit the return value to 2 decimal places
	return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44
