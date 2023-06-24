data = [('Joe', '393939333'), ('Ben', '9393933333'), ('Mark', '393939333'),
        ('Jack', '298283833'), ('Ben', '8747474747'), ('Mark', '872727333')]

customers = {}

for name, phone in data:
    phones = customers.get(name, [])
    phones.append(phone)
    customers[name] = phones

for name, phones in sorted(customers.items()):
    phones_st = ','.join(phones)     # join all phones with , separator
    print(f"{name:15} {phones_st}")
