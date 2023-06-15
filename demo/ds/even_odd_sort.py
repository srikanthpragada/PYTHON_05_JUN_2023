# Take numbers from user and then display even and odd numbers in sorted order

evens = []
odds = []

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

for n in sorted(evens) + sorted(odds):
    print(n)
