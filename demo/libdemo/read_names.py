f = open("names.txt", "rt")

for n in f.readlines():
    # print(n, end='')
    print(n.strip())

f.close()
