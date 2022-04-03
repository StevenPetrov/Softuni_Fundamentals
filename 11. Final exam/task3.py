line = input().split(' | ')
testing = input().split(' | ')
command = input()
d = dict()

for x in line:
    x = x.split(': ')
    key = x[0]
    value = x[1]
    if key in d:
        d[key].append(value)
    else:
        d[key] = []
        d[key].append(value)

if command == 'Hand Over':
    for x in d:
        print(x, end=' ')
if command == 'Test':
    for x in testing:
        if x in d.keys():
            print(f'{x}:')
            for y in d[x]:
                print(f' -{y}')