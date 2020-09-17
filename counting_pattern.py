
counts = dict()
print('Enter a line of text:')
line = input()

words = line.rstrip().split()

print('\nWords:',words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts:',counts)