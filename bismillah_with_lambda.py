
my_expression = lambda a,b,c: a+b+c
print(my_expression(1,2,3))

# normal method
my_list = []
for number in range(0,100):
    if number % 2 == 0:
        my_list.append(number)
print(my_list)

# using list comprehension
new_list = [number for number in range(0,1000) if number % 2 == 0]
print(new_list)