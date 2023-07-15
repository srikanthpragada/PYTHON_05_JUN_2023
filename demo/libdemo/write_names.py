names = ['Steve Jobs', 'Larry Ellison', 'Bill Gates', 'Elon Musk', 'Peter Thiel']

with open("names.txt", "wt") as f:
    for n in names:
        f.write(n + "\n")


