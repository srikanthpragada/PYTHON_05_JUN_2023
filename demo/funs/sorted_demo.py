nums = [10, 11, 22, -34, 56, -77, 88]

for v in sorted(nums, key=abs):
    print(v)
