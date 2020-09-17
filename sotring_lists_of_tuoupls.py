
d = {
    'ashik':10,
    'abbu':1,
    'ammu':100
}

print("Unsorted list:")
print(d.items())
print("Sorted list:")
print(sorted(d.items()))

for k,v in sorted(d.items()):
    print(f"key:{k}--value:{v}")

dc = {'a':10,'b':22,'c':1}
print(sorted(dc.items()))