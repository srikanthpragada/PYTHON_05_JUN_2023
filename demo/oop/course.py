class Course:
    taxrate = 18

    def __init__(self, name, fee=5000, duration=36):
        self.name = name
        self.fee = fee
        self.duration = duration

    def getnetfee(self):
        return self.fee + self.fee * Course.taxrate // 100


c = Course("AWS", 5000, 24)
c = Course("AWS", duration=24)
print(c.getnetfee())
