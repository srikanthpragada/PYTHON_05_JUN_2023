f = open("names.txt", "rt")

sorted_names = sorted(f.readlines())
for idx, name in enumerate(sorted_names, start=1):
    print(f"{idx:2} {name.strip()}")

f.close()
