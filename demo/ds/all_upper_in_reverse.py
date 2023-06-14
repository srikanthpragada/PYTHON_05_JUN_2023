# Print all uppercase letters in reverse order

st = "How are you Doing Today"

for c in st[::-1]:
    if c.isupper():
        print(c, end='')
