
aliens = []
print("making documents for the 30 aliens")
for alien_number  in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)

print("\nShowing the first 5 aliens")
for alien in aliens[:5]:
	print(alien)
print("...")

print(f"\nTotal number of aliens : {len(aliens)}")

print("Changing the status of first 3 aliens")
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

print("\nAgain showing the first 5 aliens")
for alien in aliens[:5]:
	print(alien)
print("...")