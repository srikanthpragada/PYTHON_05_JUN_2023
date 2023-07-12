num = input("Enter number :")
try:
    n = int(num)
    print(100 / n)
except Exception as ex:   # catch all
    print("Error ->", ex )

print("The End")
