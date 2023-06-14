# Sort marks in desc order
marks = []  # Empty list

while True:
    n = int(input("Enter marks [-1 to stop] :"))
    if n == -1:
        break
    marks.append(n)

# marks.sort(reverse=True)

for n in sorted(marks, reverse=True):
    print(n, end=' ')
