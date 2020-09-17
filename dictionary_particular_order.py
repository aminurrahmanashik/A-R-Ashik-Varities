
favourite_lannnguages = {
	'jen':'python',
	'sarah':'c',
	'edward':'reby',
	'phill':'python'
	}

for name in sorted(favourite_lannnguages.keys()):
	print(f"{name.title()}, thank you for taking the course!")


# sorted with values
print("\nThe folloeing items have been mentioned:")
for language in sorted(favourite_lannnguages.values()):
	print(language.title())

print("\nUsing the set to ensure non-repeatitve list:")
for language in set(sorted(favourite_lannnguages.values())):
	print(language.title())

# directly making a set
languages = {'python','ruby','python','c'}
print(languages)