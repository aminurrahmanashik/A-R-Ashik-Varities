import re
# using find method,(variable_name.method)
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# using regular expression,(library_method.function)
print("\n\n\n\n\n\nUsing regular expressions:")
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:',line):
        print(line)