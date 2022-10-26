

class Person:

    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = None


person = Person('Bob')

print(person.first_name) # Bob


print("before assigning to last_name", hasattr(person, "last_name"))

person.last_name = "Smith"

print("after assigning to last_name", hasattr(person, "last_name"))

delattr(person, "last_name")

print("after deleting last_name", hasattr(person, "last_name"))
