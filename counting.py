
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
message = " "
while message != 'quit':
    message = input('Prees any key to continue!\n')
    print(f"You entered: {message}")
print("Quited Successfully!")

# this code will not allow to print the message "quit" as we used an extra condition
message = " "
print("\nAgain come back")
while message != 'quit':
    message = input('Prees any key to continue!\n')
    if message != 'quit':
        print(f"You entered: {message}")
print("Quited Finally!")
