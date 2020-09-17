

print("Use of continue statement inside the loop")
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

print("Another way of for loop")
x = 0
while x <= 5:
    x += 1
    print(x)