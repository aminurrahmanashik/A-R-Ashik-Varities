
data = "From alumia@hudai.ac.gd Sat Jan 5 12:42:34 2020"

atpos = data.find('@')
print(atpos)


"""This is all about to find the space position."""
sppos = data.find(' ',atpos)
print(sppos)

"""This is to print the sliced part"""
host = data[atpos+1 : sppos]
print(host)

