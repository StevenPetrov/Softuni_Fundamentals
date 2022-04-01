d = {}
n = int(input())

for x in range(n):
    key = input()
    value = input()
    if key in d:
        d[key] += (', ' + value)
    else:
        d[key] = value

for x in d:
    print(f"{x} - {d[x]}")
