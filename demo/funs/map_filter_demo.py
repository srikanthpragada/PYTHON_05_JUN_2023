nums = ["10", "-10", "40", "-50", "60", "30", "20"]


def ispositive(n):
    return n > 0


values = map(int, nums)
pos_values = filter(ispositive, values)
print(sum(pos_values))

# using list comprehension
pos_values = [int(v) for v in nums if int(v) > 0]
print(sum(pos_values))
