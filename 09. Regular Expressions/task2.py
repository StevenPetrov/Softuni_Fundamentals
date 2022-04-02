# import re
#
# numbers = input()
#
# nums = re.findall(r'\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b', numbers)
#
# print(', '.join(nums))

import re

numbers = input()

nums = re.finditer(r'\+359([ -])2\1\d{3}\1\d{4}\b', numbers)

for x in nums:
    print(x.group(), end=', ')