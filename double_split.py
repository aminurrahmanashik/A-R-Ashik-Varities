
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if not line.startswith('From'): continue
    email = words[1]
    pieces = email.split('@')
    print(pieces[1])

