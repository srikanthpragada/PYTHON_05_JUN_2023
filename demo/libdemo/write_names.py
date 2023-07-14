names = ['Steve Jobs', 'Larry Ellison', 'Bill Gates', 'Elon Musk', 'Peter Thiel']

f = open("names.txt", "wt")

for n in names:
    f.write(n + "\n")

f.close()