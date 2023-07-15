# take customer name and display email address

with open("customers.txt", "rt") as f:
    name = input("Enter name :")
    for line in f:
        parts = line.split(",")
        if len(parts) < 2:
            continue     # ignore line as it is not in valid format

        if parts[0].upper() == name.upper():
            print('Email : ', parts[1])
            exit(0)  # terminate program

    print("Sorry! Name not found!")
