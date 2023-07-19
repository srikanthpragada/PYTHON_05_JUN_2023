import re

with  open("phones.txt", "rt") as f:
    phones = set()
    for line in f:
        m = re.search("\d{10,}", line)
        if m is None:  # not found, ignore line
            continue

        phone = m.group()
        if len(phone) == 10:
            phones.add(phone)

for p in sorted(phones):
    print(p)
