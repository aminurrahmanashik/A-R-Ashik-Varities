
current_users = ['ullala','challala','lamuna','motu','nutara']
new_users = ['lamuna','malala','shakaal','motu','patlu']

for new_user in new_users:
	if(new_user in current_users):
		print(f"\nSorry! this name: {new_user.title()} is taken already.")
	else:
		print(f"\n{new_user} is available.")