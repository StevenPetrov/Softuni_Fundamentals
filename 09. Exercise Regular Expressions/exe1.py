import re

nums = []

while True:

    text = input()

    if not text:
        break

    filtered = re.findall(r'\d+', text)

    nums += filtered

print(' '.join(nums))
