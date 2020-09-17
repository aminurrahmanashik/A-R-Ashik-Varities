
fhand = open('romeo.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

lst = list()
lst = [(v,k) for k,v in counts.items()]

lst = sorted(lst,reverse=True)
print(lst)

for v,k in lst:
    print(k,v)
