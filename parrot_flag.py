


# here 'acive' is the flag variable
active = True
message = " "
while active:
    message = input()

    if message == 'quit':
        active = False
    else:
        print(f"You typed: {message}\n")
print("U quited :(")