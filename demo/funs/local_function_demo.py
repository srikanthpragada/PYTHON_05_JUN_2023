g = 1000  # global variable


def f1():
    global g
    g = 500  # change global variable
    a = 1  # enclosing variable

    # Local function
    def f2():
        b = 10  # local variable
        nonlocal a
        a = 2  # change enclosing variable
        print(g, a, b)

    f2()


f1()
