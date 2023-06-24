st = "how do you do today and how you were yesterday how you will be tomorrow"

words = st.split(" ")
for w in set(words):
    print(w, words.count(w))

