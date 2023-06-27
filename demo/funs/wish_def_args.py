def wish(user='Guest', message='Hello'):
    print(message, user)


wish('Bob', 'Hi')  # positional arguments
wish(message='Hello', user='Roberts')  # keyword arguments
wish('linda', message='Good Morning')  # mixed
wish('Steve')
wish(message='Hi')
