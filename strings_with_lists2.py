
""" split() will cover the extra spaces as well"""

line = 'A lot       of spaces'
etc = line.split()
print(etc)
# nothing changes if there is no option for spaces
line = 'AminurRahmanAshik'
etc = line.split()
print(etc)

# we can specify to spilt() inside the string
line = 'first;second;third'
etc = line.split(';')
print(etc)