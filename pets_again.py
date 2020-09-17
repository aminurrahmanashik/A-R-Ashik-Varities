

# basically it's an operation on :  remove() inside while loop
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
print("We want to remove the duplicates from the list.")
while 'cat' in pets:
    pets.remove('cat')
print(pets)