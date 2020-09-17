
def full_email(people):
    result = []
    for email,name in people:
        result.append("{}<{}>".format(name,email))
    return result

print(full_email([('ashik@gmail.com','Ashik'),('abir@gmail.com','Kesra')]))
