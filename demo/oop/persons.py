class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show(self):
        print(self.name)
        print(self.email)

    def set_email(self, newemail):
        self.email = newemail


class Student(Person):
    def __init__(self, name, email, course, college):
        super().__init__(name, email)
        self.course = course
        self.college = college

    def show(self):
        super().show()  # call super class version
        print(self.course)
        print(self.college)

    def change(self, course=None, college=None):
        if course is not None:
            self.course = course

        if college is not None:
            self.college = college


s = Student("Scott", "scott@gmail.com", "CS", "Stanford")
s.change(college="MIT")
s.set_email("scott@yahoo.com")
s.show()
