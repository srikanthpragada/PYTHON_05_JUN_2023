def show(*args, **kwargs):
    for v in args:
        print(v)
        
    for k, v in kwargs.items():
        print(k, v)


show(10, 20, msg="Hi", user='Joe')
