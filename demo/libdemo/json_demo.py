import json

 
class Person:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age


p1 = Person("Larry", 'larry@gmail.com', 40)
print(p1.__dict__)
print(json.dumps(p1.__dict__))    # JSON serialization


