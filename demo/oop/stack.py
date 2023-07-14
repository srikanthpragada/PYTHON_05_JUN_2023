class Stack_Iterator:
    def __init__(self, data):
        self.data = data
        self.pos = len(data) - 1

    def __next__(self):
        if self.pos >= 0:
            self.pos -= 1
            return self.data[self.pos + 1]
        else:
            raise StopIteration


class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    @property
    def length(self):
        return len(self.data)

    def clear(self):
        self.data.clear()

    def __iter__(self):
        return Stack_Iterator(self.data)


s = Stack()
s.push(10)
s.push(20)
s.push(30)
# print(s.pop())
# print(s.peek())
# print(s.length)    # property

for n in s:
    print(n)
