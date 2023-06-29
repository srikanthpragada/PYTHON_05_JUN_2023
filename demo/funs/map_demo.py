nums = [10, 11, 22, -34, 56, -77, 88]
data = ["10", "20", "30"]

values = ["abc123", "84abc", "r56ue87"]


def extract_number(s):
    n = ""
    for c in s:
        if c.isdigit():
            n += c

    return int(n)


# print(extract_number("3737abcd83"))

for n in map(abs, nums):
    print(n)

print(sum(map(int, data)))

for v in map(extract_number, values):
    print(v)
