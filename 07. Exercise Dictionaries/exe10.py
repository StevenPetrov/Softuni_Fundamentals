d = {}

while True:
    command = input()
    if command == 'End':
        break
    command = command.split(' -> ')
    company = command[0]
    employee_id = command[1]
    if company not in d:
        d[company] = []
    if employee_id not in d[company]:
        d[company].append(employee_id)

for x in d:
    print(x)
    for y in d[x]:
        print(f'-- {y}')
