wagons = [0 for x in range(int(input()))]

while True:
    command = input()
    if command == 'End':
        break
    elements = command.split(' ')
    if elements[0] == 'add':
        wagons[-1] += int(elements[1])
    if elements[0] == 'insert':
        wagons[int(elements[1])] += int(elements[2])
    if elements[0] == 'leave':
        wagons[int(elements[1])] -= int(elements[2])

print(wagons)
