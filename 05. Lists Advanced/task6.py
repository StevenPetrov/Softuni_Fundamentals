nums = list(map(int, input().split(', ')))


index_even = list()

for x in nums:
    if x % 2 == 0:
        a = nums.index(x)
        index_even.append(a)

print(index_even)
