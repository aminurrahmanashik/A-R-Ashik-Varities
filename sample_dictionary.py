
alien_0 = {'color': 'pink','quality':'virgin','points': 5}
print(alien_0)

print('printing the respective values.')
print(alien_0['color'])
print(alien_0['quality'])

new_points = alien_0['points']
print(f"\nYou just earned {new_points} points!")

print('Adding a new values:')
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)