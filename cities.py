

cities  = {
	'dhaka' : {
	'country' : 'bangladesh',
	'population' : '161.4 million'
	},
	'mumbai' : {
	'country' : 'india',
	'population' : '1.353 billion'
	},
	'karachi' : {
	'country' : 'pakistan',
	'population' : '212.2 million'
	}
}

for city,infos in cities.items():
	print(f"\nI know some information about {city.title()}")
	print(f"It is belongs to: {infos['country'].title()}")
	print(f"Over {infos['population']} people live here!")


