
def fun():
    print("Function")


fun2 = fun

print(type(fun))
print(id(fun))
fun()
fun2()
