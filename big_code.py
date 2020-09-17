
fname = input('Enter file:')
handle = open(fname)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

BigCount = None
BigWord = None
for word,count in counts.items():
    if BigCount is None or count > BigCount:
        BigCount = count
        BigWord = word

print(BigWord,BigCount)