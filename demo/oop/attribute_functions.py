class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Bob", 40)
print(getattr(p, 'age'))
print(getattr(p, 'gender', 'm'))

print(hasattr(p, 'gender'))

setattr(p, 'gender', 'male')
print(getattr(p, 'gender'))

delattr(p, 'gender')
print(hasattr(p, 'gender'))
