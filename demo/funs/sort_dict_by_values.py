d = {1: 10, 3: 15, 2: 5, 4: 50, 5: 3}

for k, v in sorted(d.items(), key=lambda t: t[1]):
    print(k, v)
