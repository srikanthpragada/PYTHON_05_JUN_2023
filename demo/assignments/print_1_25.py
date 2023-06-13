# Nested loop demo

n = 1
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{n:3}", end=' ')
        n += 1

    print()  # go to next line