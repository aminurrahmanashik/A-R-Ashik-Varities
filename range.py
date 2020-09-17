
# basically to make ranging of something, we can use range() method

# with be iterated through 1  to 5
for value in range(1,6):
 print(value)

#  kono ekta value ranging k jdi amra list e convert krte chai then
# amra list use krte pari
numbers = list(range(2,11,2))
print(numbers)

squares = []

for value in range(1,11):
	squares.append(value**2)
print(squares)

# it will give the max element from the generated list
print(max(squares))

# it will give the max element from the generated list
print(min(squares))

# this is called 'list comprehension'
# here one line works for other 2/3 lines of code
square_short = [value**2 for value in range(1,6)]
print(square_short)

