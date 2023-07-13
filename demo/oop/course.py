class InvalidFeeError(Exception):
    def __init__(self, fee):
        self.fee = fee

    def __str__(self):
        return f"Invalid Course Fee {self.fee}. It must be >= 0"


class Course:
    taxrate = 18

    def __init__(self, name, fee=5000, duration=36):
        if fee < 0:
            raise InvalidFeeError(fee)

        if duration <= 0:
            raise ValueError(f"Invalid Duration --> {duration}. It must be > 0")

        self.name = name
        self.fee = fee
        self.duration = duration

    def getnetfee(self):
        return self.fee + self.fee * Course.taxrate // 100


c = Course("AWS", -5000, 30)

c = Course("AWS", duration=24)
print(c.getnetfee())
