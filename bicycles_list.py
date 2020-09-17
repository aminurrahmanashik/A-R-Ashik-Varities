names = ['tarek', 'couser','reman','sohail']
names[0] = 'ashik'
print(names)
message = f"Assalamu Alaikum!,{names[0].upper()}"
print(message)

# it will print the list in reverse index
print(names[-1])
print(names[-3])

## new element at end of the list
names.append('abir')
print(names)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('runner')
motorcycles.append('chinese')
motorcycles.append('ford')
motorcycles.append('walton')
print(motorcycles)

# insert allows to add at any position
motorcycles.insert(1,'ducati')
print(motorcycles)

# if u use (out of range) to add elements,It'll add at the end then
motorcycles.insert(100,'hero')
print(motorcycles)

# del is used to delete the items from a list with respective postion 
del motorcycles[4]
print(motorcycles)

# by default, pop() is just like popping(deleting) out the last element from the list
# we can work with the deleting element afterwords

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

#popping from any position
third_owned = motorcycles.pop(2)
print(f"The third motorcycle I owned was a {third_owned.title()}")
print(motorcycles)

motorcycles.insert(2,'ducati')
print(motorcycles)

# romeve used to erase an element without knowing it's position
# it will only remove the first matched element of the list
motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'ford'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"{too_expensive} is too expensive for me. :(")
