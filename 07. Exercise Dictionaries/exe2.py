d= {}

while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())
    if resource in d:
        d[resource] += quantity
    else:
        d[resource] = quantity

for x in d:
    print(f"{x} -> {d[x]}")