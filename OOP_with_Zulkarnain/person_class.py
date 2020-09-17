
class Person:
    def __init__(self,name : str,year_of_birth : int,height : int = None):
        # to treat the instance variables as private,use __ before their name
        self.__person_name = name
        self.__person_dob = year_of_birth
        self.__person_height = height


    def get_year_of_birth(self):
        return self.__person_dob

    def get_name(self):
        return self.__person_name

    def set_name(self,new_name):
        if(self.__has_any_number(new_name)):
            print("Error! Number cannot be as a name :(")
            return
        self.__person_name = new_name

    def __has_any_number(self,string):
        return "0" in string

    def get_summary(self):
        return f"Name: {self.__person_name}, DOB: {self.__person_dob}, Height: {self.__person_height if self.__person_height is not None else 'Invalid'}"



person_list = [Person("A R Ashik", 1998, 72),
               Person("Abul MAl", 1948, 89),
               Person("Pagla", 1988, 63),
               Person("Hasem",1956),
               Person("Abir", 2000, 69),
               Person("Lallu",1943),
               Person("Kashem", 1968, 70)]


# for person in person_list:
#     if person.get_year_of_birth() >= 1940 :
#         print(person.get_summary())


# subclass Student of Person class
class Student(Person):
    def __init__(self, name: str, year_of_birth: int,email_id: str,student_id: str):
        super().__init__(name, year_of_birth)
        self.id = student_id
        self.email = email_id

    def get_summary(self):
        return f"Name: {self.get_name()}, Email: {self.email}, Birth: {self.get_year_of_birth()}"

    def __str__(self):
        return self.get_summary()
        # return f"Name: {self.get_name()}, Email: {self.email}, Birth: {self.get_year_of_birth()}"


    # def __repr__(self):
    #      return self.get_summary()
        # return f"Name: {self.get_name()}, Email: {self.email}, Birth: {self.get_year_of_birth()}"



# subclass Teacher of Person class
class Teacher(Person):
    def __init__(self,name: str, year_of_birth: int,department: str):
        super().__init__(name, year_of_birth)
        self.dept = department

    def get_summary(self):
        return f"{self.get_name()} is a teacher."

# student = Student("Yousuf Sikder",2009,"fayaz@gmail.com","1704013_fayaz")
# print(student)
# student.set_name("Fayaz")
# print(student)

new_person_list = [Person("Ashik", 1998),
              Student("Fayaz", 2009, "yousufsikderfayaz@gmail.com", "1704013_fayaz"),
              Teacher("Amanullah", 1977, "CSE")]

for person in new_person_list:
    # print(person.get_name())
    print(person.get_summary())


"""creating a new class which acts as a struct in C programming,It's a separate class without being super/sub class"""
class PlainClass:
    pass

#creating an object
abc = PlainClass()
abc.age = 30
abc.name = "Ashik"

print(abc.age)
print(abc.name)

