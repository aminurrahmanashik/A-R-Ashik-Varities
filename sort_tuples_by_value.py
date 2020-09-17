
c = {'a': 10,'b': 1,'c': 22}
print(c)

tmp1 = list()
for k,v in c.items():
    tmp1.append((v,k))

print(f"Reversing the dictionary:{tmp1}")
# used [reversed = True] to let it go for descending order like-> 22,10,1
tmp2 = sorted(tmp1,reverse = True)
print(f"The ultimate result:{tmp2}")