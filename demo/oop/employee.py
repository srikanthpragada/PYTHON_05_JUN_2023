class Employee:
    # class attribute or static attribute
    hraper = 25

    @staticmethod   # decorator
    def change_hraper(newhraper):
        Employee.hraper = newhraper

    # Constructor
    def __init__(self, name, job, salary):
        # Object Attributes
        self.name = name
        self.job = job
        self.salary = salary

    # Method

    def get_net_salary(self):
        return self.salary + self.salary * Employee.hraper // 100

    def change_job(self, newjob):
        self.job = newjob

    def hike_salary(self, hikeper):
        self.salary = self.salary + (self.salary * hikeper // 100)

    def show(self):
        print(f"Name   :   {self.name}")
        print(f"Job    :   {self.job}")
        print(f"Salary :   {self.salary}")


# Calling static method using classname
Employee.change_hraper(30)

e1 = Employee("Bob", "programmer", 60000)  # create object
# print(e1.__dict__)
e1.hike_salary(30)
print(e1.get_net_salary())
e1.show()

e2 = Employee("Scott", "dba", 100000)
e2.change_job("Data Eng.")
print(e2.get_net_salary())
