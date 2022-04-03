stops = input()

while True:
    command = input()
    if command == 'Travel':
        break
    command = command.split(':')
    action = command[0]

    if action == 'Add Stop':
        index = int(command[1])
        string = command[2]
        if 0 <= index <= len(stops):
            stops = stops[:index] + string + stops[index:]

    if action == 'Remove Stop':
        from_ = int(command[1])
        end_ = int(command[2])

        if 0 <= from_ <= end_ < len(stops):
            stops = stops[:from_] + stops[end_ + 1:]

    if action == 'Switch':
        old = command[1]
        new = command[2]
        if old in stops:
            stops = stops.replace(old, new)
    print(stops)

print(f'Ready for world tour! Planned stops: {stops}')
