# Count python files starting from the given folder
import os
import sys

if len(sys.argv) >= 2:
    startdir = sys.argv[1]  # Starting directory
else:
    startdir = '.'    # Assume current directory as start directory when not given

if len(sys.argv) >= 3:
    ext = sys.argv[2]  # extension of file
else:
    ext = '.py'        # Assume .py extension when not given

entries = os.walk(startdir)
count = 0

for dirname, dirs, files in entries:
    for f in files:
        if f.endswith(ext):
            count += 1

print("Count =", count)
