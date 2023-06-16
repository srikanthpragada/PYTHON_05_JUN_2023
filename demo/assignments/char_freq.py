st = "Javascript and Java are not same"

chars_visited = []
for c in st:
    if c not in chars_visited:
        print(c, st.count(c))
        chars_visited.append(c)
