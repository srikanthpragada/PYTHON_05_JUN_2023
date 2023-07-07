class Counter:
    def __init__(self, start=0):
        self.start = start
        self.value = start

    def inc(self, step=1):
        self.value += step

    def dec(self, step=1):
        self.value -= step

    def reset(self):
        self.value = self.start

    def getvalue(self):
        return self.value


c = Counter()   # create an instance/object 
c.inc()
print(c.getvalue())
c.inc(5)
print(c.getvalue())
c.reset()
print(c.getvalue())
