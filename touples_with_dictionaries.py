
d = dict()
d['ashik'] = 1
d['amin'] = 2
for (k,v) in d.items():
    print(f"[{k.title()}] = {v}")


tups = d.items()
print(tups)

print((1,2,3) < (1,2,3))
# the l is less than m and so that's why this entire thing is True
print(('ashik','asif') < ('ashik','asad'))