lsort = ['' for x in range(11)]

command = input()

while command != 'End':
    fragment = command.split('-')
    lsort[(int(fragment[0]))] = fragment[1]
    command = input()

final = [x for x in lsort if x != '']
print(final)
