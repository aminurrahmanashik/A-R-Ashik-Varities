 
players = ['tamim','sakib','mushfiq','mahmudullah','mashrafe']
print(players)

# printing the plyers name with a segment/portion
print('\nprinting the plyers name with a segment/portion')
print(players[0:3]) # for 0,1,2b

print(players[1:3]) # for 1,2

# using the shortcut,this command will work for 0,1,2 
print('\nusing the shortcut,this command will work for 0,1,2 ')
print(players[:4])

#  a slice that includes the end of a list
print('\na slice that includes the end of a list')
print(players[2:])

# making the list to print after every 2 elements
print('\nmaking the list to print after every 2 elements')
print(players[0:5:2])

# by default taking upto the end of the list with interval/skip of 2
print(f"by default taking upto the end of the list and interval of 2")
print(players[0::2])

#  to do output the last three players on the roster
print('\noutput of the last three players on the roster')
print(players[-3:])

# working with loop and silce of a list
print('\nHere are the first three players on my team')
for player in  players[:3]:
   print(player.title())

# by default copying list into a new list
print('\nby default copying list into a new list')
print(f"but any change in list will not effect the copied list as both will point the same list")
new_players = players
print(new_players)

# see the proof
print('\nsee the proof')
players.append('miraj')
print(players)
print(new_players)


# we can do the same as
print('\nwe can do the same as this statement, but any change in main list will affect the copied list')
new_list = players[:]
print(new_list)

# to  prove that we actually have two separate lists
# we’ll add a new player to each list
players.append('ashik')
new_list.append('abir')
print('\nto  prove that we actually have two separate lists')
print('players:')
print(players)
print('new_list:')
print(new_list)

