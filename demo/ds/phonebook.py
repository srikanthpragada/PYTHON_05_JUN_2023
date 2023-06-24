data = [('Joe', '393939333'), ('Ben', '9393933333'), ('Mark', '393939333'),
        ('Jack', '298283833'), ('Ben', '8747474747')]

customers = {}

for name, phone in data:
    customers[name] = phone

for name, phone in sorted(customers.items()):
    print(f"{name:15} {phone}")
