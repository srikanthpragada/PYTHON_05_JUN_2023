import re

with open("test.txt", "rt") as f:
    contents = f.read()

new_contents = re.sub(" +", " ", contents)
new_contents = re.sub("\n+", "\n", new_contents)

with open("test.txt", "wt") as f:
    f.write(new_contents)
