class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return str(self.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __float__(self):
        return float(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)


c1 = Circle(10)
c2 = Circle(20)
c3 = Circle(20)

print(c1)  # c1.__str__()

print(c2 == c3)  # c2.__eq__(c3)

print(c2 > c1)  # c2.__gt__(c1)

print(float(c1) + float(c2))

circles = [Circle(5), Circle(15), Circle(10)]

for c in sorted(circles):
    print(c)

c4 = c1 + c2   #  c1.__add__(c2)
print(c4)