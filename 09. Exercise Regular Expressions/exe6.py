import re

email_list = []

while True:

    text = input()

    if not text:
        break

    pattern = r'www.[a-zA-Z0-9]+[-]*[a-zA-Z0-9]+[-]*[a-zA-Z0-9]+[.][a-zA-Z]+[.]*[a-zA-Z]*[.]*[a-zA-Z]*'

    emails = re.findall(pattern,text)

    email_list += emails

print('\n'.join(email_list))