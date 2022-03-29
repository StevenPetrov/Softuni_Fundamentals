marker = list(map(int, input().split()))
command = input()
while command != 'End':
    command = command.split()
    index = int(command[1])
    value = int(command[2])
    if command[0] == 'Shoot':
        if 0 <= index < len(marker):
            marker[index] -= value
            if marker[index] <= 0:
                marker.remove(marker[index])
        else:
            pass
    if command[0] == 'Add':
        if 0 <= index < len(marker):
            marker.insert(index, value)
        else:
            print("Invalid placement!")
    if command[0] == 'Strike':
        if index + value < len(marker) and index - value >= 0:
            marker = marker[:index-value]+marker[index+value+1:]
        else:
            print("Strike missed!")
    command = input()
final = list(map(str, marker))
print('|'.join(final))
