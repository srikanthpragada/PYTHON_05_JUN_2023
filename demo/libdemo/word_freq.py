st = """This is first line
This is second line;
We have more     spaces     between words   now!!
However, this is fine    with     Regular Expressions
"""

import re

words = re.findall("\w+", st)

for w in sorted(set(words)):
    print(f"{w:10} - {words.count(w):2}")
