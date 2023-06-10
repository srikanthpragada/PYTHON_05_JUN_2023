# Take a number and check whether it is divisible by 3 and 5

num = int(input("Enter a number :"))
if num % 3 == 0:
    if num % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Divisible by None")
