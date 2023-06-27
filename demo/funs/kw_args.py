def show(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


show(a=10, b=20, msg='Hi')
show(x=10, y=20, z=30)
