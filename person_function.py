
def build_person(first_name,last_name):
    """Return a dictioanry of information abiut a person"""
    person = {'first':first_name,'last':last_name}
    return person

# it's basically an returning a list
hujur = build_person('aminur','rahman')
print(hujur)
# with third parameter with 'NONE' value'
def build_person(first_name,last_name,age = None):
    """Return a dictioanry of information abiut a person"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

# it's basically an returning a list
hujur = build_person('aminur','rahman',21)
print(hujur)

hujur = build_person('aminur','rahman',21)
print(hujur)
