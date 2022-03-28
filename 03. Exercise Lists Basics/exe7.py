l = input().split(' ')

while True:
    command = input()
    if command == 'No Money':
        break
    if 'OutOfStock' in command:
        command = command[11:]
        if command in l:
            l = [word.replace(command, 'None') for word in l]
    if 'Required' in command:
        command_new = command[9:-2]
        index = int(command[-1])
        if index < len(l):
            l[index] = command_new
    if "JustInCase" in command:
        command = command[11:]
        l.pop()
        l.append(command)

while 'None' in l: l.remove('None')

l = ' '.join(l)

print(l)
