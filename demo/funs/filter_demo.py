nums = [10, 11, 22, 34, 56, 77, 88]


def iseven(n):
    return n % 2 == 0


for n in filter(iseven, nums):
    print(n)

for n in filter(str.isupper, "AbcDef"):
    print(n)
