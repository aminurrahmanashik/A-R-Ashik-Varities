
values = []
for n in range(1,100001,2):
  values.append(n)

print(f"The sum is:{sum(values)}")
print(f"The min is:{min(values)}")
print(f"The max is:{max(values)}")
print(values)

print('\n\n\n')
numbers = list(range(0,10001,2))
print(f"The sum is:{sum(numbers)}")
print(f"The min is:{min(numbers)}")
print(f"The max is:{max(numbers)}")
print(numbers)

values_cube = []
for n in range(1,11):
  values_cube.append(n**3)
print(values_cube)

print("list comprehension")

print([n**3 for n in range(1,11)])