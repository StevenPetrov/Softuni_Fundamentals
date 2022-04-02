import re
l = []
pattern = r'\b[_](?P<sort>[a-zA-Z0-9]+)\b'

text = input()

words = re.finditer(pattern, text)

for x in words:
    l.append(x.group('sort'))

print(','.join(l))