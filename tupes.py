
fhand = open('romeo.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

lst = list()
for k,v in counts.items():
    lst.append((v,k))

lst = sorted(lst,reverse = True)

for v,k in lst[:10]:
    print(k,v)

"""
using shorthand version to print reverse
"""
c = {'a': 10,'b': 1,'c': 22}
print(sorted([(v,k) for k,v in c.items()],reverse=True))