

a,b = map(int, input().split())

if a < b:
    c = a
else :
    c = b

factorial = 1
if int(c) >= 1:
    for i in range (1,int(c)+1):
        factorial = factorial * i
        
print(factorial)
