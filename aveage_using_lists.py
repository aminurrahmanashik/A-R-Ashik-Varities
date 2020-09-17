
namelist = list()

while True:
    inp = input("Enter a number:")
    if inp == 'done': break
    namelist.append(float(inp))


average = sum(namelist)/len(namelist)
print(average)