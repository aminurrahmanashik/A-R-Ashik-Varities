
import re

fname = open('mbox-short.txt')
numlist = list()

for line in fname:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1 : continue
    num = float(stuff[0]) # we need to do such,cz it's a list actually
    numlist.append(num)

print('Maximum:',max(numlist))