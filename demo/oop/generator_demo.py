def numbers():
    for n in range(1, 6):
        yield n


n = numbers()
print(n)
print(next(n))
print(next(n))
print("The End")
