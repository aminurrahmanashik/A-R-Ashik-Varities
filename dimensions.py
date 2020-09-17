
dimensions = (200,50)
print(dimensions)

print(dimensions[0])
print(dimensions[1])

print('\ntouples can be denoted as:')
my_t = (3,)
print(my_t)

print('\nloopinng through the entire touple')
for dimension in dimensions:
 print(dimension)

# doesn't rasise any error because of reassining
print('\ndefinning the dimension as a whole(new)')
dimensions = (400,100)
for dimension in dimensions:
 print(dimension)

