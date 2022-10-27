""" class methods module """

class Person:
    """ person class """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        """ full name method"""
        return f"{self.last_name}, {self.first_name}"

    @classmethod
    def from_name(cls, full_name):
        """ create person from name """
        return Person(*full_name.split(" "))

person = Person("Bob", "Smith")
print(person.full_name())

print(Person.from_name("Linda Thompson").full_name())