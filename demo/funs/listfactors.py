# Take a number on command line and display factors
import sys

if len(sys.argv) < 2:
    print("Usage: python listfactors.py  <number>")
    exit()  # stop program

num = int(sys.argv[1])
found = False
for i in range(2, num // 2 + 1):
    if num % i == 0:
        found = True
        print(i, end=' ')

if not found:
    print("No factors found as number is prime!")