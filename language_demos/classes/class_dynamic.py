
class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return self.first_name + " " + self.last_name


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def record_label(self):
        return  self.last_name + ", " + self.first_name        


Student.full_name = Person.full_name

# def constructor(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name

# def record_label(self):
#     return  self.last_name + ", " + self.first_name


# Student = type("Student", (object, ), {
#     "__init__": constructor,
#     "full_name": Person.full_name,
#     "record_label": record_label
# })

student = Student("Bob", "Smith")
print(student.full_name())
print(student.record_label())