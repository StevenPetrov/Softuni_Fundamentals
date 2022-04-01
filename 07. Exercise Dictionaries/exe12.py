d = {}
banned = ''
while True:
    command = input()
    if command == 'exam finished':
        break
    if 'banned' in command:
        command = command.split('-')
        banned = command[0]

    if 'banned' not in command:
        command = command.split('-')
        username = command[0]
        language = command[1]
        points = command[2]

        if language not in d:
            d[language] = username+'-'+points
        else:
            d[language] += '@'+username+'-'+points


for x in d:
    names = d[x].split('@')
    d[x] = names

for x in d:
    for y in d[x]:
        if banned in y:
            pass


print(d)





