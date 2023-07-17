# Count python files starting from the given folder
import os

entries = os.walk(r"c:\classroom\jun5\demo")
count = 0

for dirname, dirs, files in entries:
    for f in files:
        if f.endswith(".py"):
            count += 1

print("Count =", count)
