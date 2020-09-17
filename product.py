
product = 1
for n in range(1,5000):
    product = product*n

print(product)

def celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x , "->" ,celsius(x))