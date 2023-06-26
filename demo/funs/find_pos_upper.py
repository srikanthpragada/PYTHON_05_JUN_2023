
def get_upper_pos(st):
    for idx, c in enumerate(st):
        if c.isupper():
            return idx

    return -1  # not found


pos = get_upper_pos("abcdefa")
if pos == -1:
    print("Not found")
else:
    print("Found at", pos)