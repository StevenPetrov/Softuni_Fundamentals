import re

text = input()

pattern = r'\b[a-zA-Z]+[._-]*[a-zA-Z0-9]+\b@\b[a-zA-Z0-9]+[-]*[a-zA-Z]+[.][a-zA-Z]+[.]*[a-zA-Z]*[a-zA-Z]\b'

emails = re.findall(pattern,text)

print('\n'.join(emails))