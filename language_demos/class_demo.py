

class Person:

    def __init__(self, first_name, last_name):
        # instance attributes
        self.first_name = first_name
        self.last_name = last_name

    # instance method
    def full_name(self):
        # return f"{self.first_name} {self.last_name}"
        return self.first_name + " " + self.last_name

    # instance method
    def record_label(self):
        return f"{self.last_name}, {self.first_name}"

class Student(Person):

    def __init__(self, student_id, first_name, last_name):
        super().__init__(first_name, last_name)
        self.student_id = student_id

    # instance method
    def info(self, extra_info):
        return f"{self.student_id} {self.last_name}, {self.first_name} {extra_info}"

# person is an instance variable
person = Person("Bob", "Smith")
print(person.full_name())
print(person.record_label())

student = Student(3, "Alice", "Thompkins")
print(student.full_name())
print(student.record_label())
print(student.info("!!!"))
print(student.first_name)

    