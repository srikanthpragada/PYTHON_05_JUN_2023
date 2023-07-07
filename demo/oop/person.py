class Person:
    def __init__(self, name, age):
        # public attribute
        self.name = name
        # private attribute
        self.__age = age


p = Person("Bob", 40)
print(p.name)
print(p.__dict__)
print(p._Person__age)
print(p.__age)
