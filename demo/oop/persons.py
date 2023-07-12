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



class Employee(Person):
    def __init__(self, name, email, job, company):
        super().__init__(name, email)
        self.job = job
        self.company = company

    def show(self):
        super().show()  # call super class version
        print(self.job)
        print(self.company)

    def change(self, job=None, company=None):
        if job is not None:
            self.job = job

        if company is not None:
            self.company = company


s = Student("Scott", "scott@gmail.com", "CS", "Stanford")
s.change(college="MIT")
s.set_email("scott@yahoo.com")
s.show()
