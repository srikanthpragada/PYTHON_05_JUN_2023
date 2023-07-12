num = input("Enter number :")
try:
    n = int(num)
    print(100 / n)
except ValueError as ex:
    print("Error ->", ex)
except ZeroDivisionError:
    print("Sorry! Zero is not a valid number")

print("The End")
