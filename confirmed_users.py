
#  start with users that need to be varfied
# and an empty list to hold confirmed users
print("Use of list with while_loop")
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Varifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nDisplaying the confirmed users")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())