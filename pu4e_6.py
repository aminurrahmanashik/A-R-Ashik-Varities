
import re
fname = open('regex_sum_514316.txt')
#print(sum([number for number in re.findall('[0-9]+',fname.read())]))
print( sum([ int(number) for number in re.findall('[0-9]+',fname.read()) ]))