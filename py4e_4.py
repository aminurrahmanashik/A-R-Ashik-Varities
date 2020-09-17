
fname = input('Enter file:')
fh = open(fname)

counts = dict()
for line in fh:
    if not line.startswith('From '): continue
    words = line.split()
    counts[words[1]] = counts.get(words[1],0) + 1


BigCount = None
BigWord = None
for word,count in counts.items():
    if BigCount is None or count > BigCount:
        BigCount = count
        BigWord = word

print(BigWord,BigCount)