import re

times = int(input())

pattern = r'^(.+)[>]([\d]{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})[<](.+)$'

for x in range(times):
    trigger = False
    word = input()
    check = re.finditer(pattern,word)
    if check:
        for x in check:
            if x.group(1) == x.group(6):
                final = x.group(2)+x.group(3)+x.group(4)+x.group(5)
                print(f"Password: {final}")
                trigger = True
    if not trigger:
        print("Try another password!")