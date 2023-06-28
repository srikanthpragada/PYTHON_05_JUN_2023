def find_differ_pos(st1, st2):
    for idx, c in enumerate(st1):
        if idx >= len(st2):  # first string is bigger than second one
            return idx

        if c != st2[idx]:    # Char do not match
            return idx

    if len(st2) > len(st1):   # second string is bigger than first one
        return len(st1)
    else:
        return -1


print(find_differ_pos("java", "jAva"))
