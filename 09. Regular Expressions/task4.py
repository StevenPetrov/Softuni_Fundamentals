import re

numbers = input()

nums = re.finditer(r'(?P<space>^|(?<=\s))-?([0]?[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))', numbers)

num_l = []

for x in nums:
    print(x.group(), end=' ')