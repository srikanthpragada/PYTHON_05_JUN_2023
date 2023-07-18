# Display word frequency for contents of a file

import re
f = open("story.txt", "rt")
st = f.read()
f.close()

words = re.findall(r"\w+", st.lower())

for w in sorted(set(words)):
    print(f"{w:15} - {words.count(w):2}")
