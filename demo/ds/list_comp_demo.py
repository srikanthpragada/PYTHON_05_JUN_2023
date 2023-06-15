square = []

for n in range(1, 10):
    square.append(n * n)

print(square)

# List comprehension
square = [n * n for n in range(1, 10)]
print(square)

# List comprehension with condition
codes = [ord(ch) for ch in "AbCdEf" if ch.isupper()]
print(codes)
