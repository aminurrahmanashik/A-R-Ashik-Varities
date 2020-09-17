
fname = input("Enter file:")
fhand = open(fname)
counts = dict()
for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    val = words[5]
    n_val = val.split(':')
    counts[n_val[0]] = counts.get(n_val[0],0)+1

for k,v in sorted(counts.items()):
    print(k,v)


