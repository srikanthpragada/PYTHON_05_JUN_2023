# Display word frequency for contents of a file

import re

f = open("story.txt", "rt")
st = f.read()
f.close()

words = re.findall(r"\w+", st.lower())

words_count = {}
for w in sorted(set(words)):
    words_count[w] = words.count(w)

for word, count in sorted(words_count.items(), key=lambda t: t[1], reverse=True)[:5]:
    print(f"{word:15} - {count:2}")
