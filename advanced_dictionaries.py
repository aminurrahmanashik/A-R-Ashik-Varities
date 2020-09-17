
favourite_lannnguages = {
	'jen':'python',
	'sarah':'c',
	'edward':'reby',
	'phill':'python'
	}

friends  = ['phill','sarah']

for name in favourite_lannnguages.keys():
	print(name.title())

	if name in friends:
		language = favourite_lannnguages[name]
		print(f"\t{name.title()}, I see you love {language.title()}!")

print("\nA new list to check whether they are a free member or not")

free_memebers = ['jamal','jen','edward','sarah']

for member in free_memebers:
	print(member.title())
	if member not in favourite_lannnguages.keys():
		print(f"Sorry {member}, you are not in the list!")
	elif member in free_memebers:
		print("\tCongratulations! you are a free memeber.")
	else:
		print(f"{member.title()} please take our poll!")
		