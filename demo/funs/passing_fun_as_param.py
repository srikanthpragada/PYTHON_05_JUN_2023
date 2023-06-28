def dosomething(task, value):
    task(value)


def square(v):
    print(v * v)


# Passing a function as parameter
dosomething(print, 100)
dosomething(square, 5)
