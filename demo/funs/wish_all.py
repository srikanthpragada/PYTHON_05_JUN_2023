def wish(*users, message='Hello'):
    # print(type(users))
    for u in users:
        print(message, u)


wish('Bob', 'Alice', 'Mike', message='Hi')
wish("Tom", "Joe")
