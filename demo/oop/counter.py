class Counter:
    instances = 0
    def __init__(self, start=0):
        self.start = start
        self.value = start
        Counter.instances += 1

    def inc(self, step=1):
        self.value += step

    def dec(self, step=1):
        self.value -= step

    def reset(self):
        self.value = self.start

    @property
    def count(self):
        return self.value


c = Counter()   # create an instance/object 
c.inc()
print(c.count)
c.inc(5)
print(c.count)
c.reset()
print(c.count)

c2 = Counter()
print(Counter.instances)