line1 = input().split(', ')
line2 = input().split(', ')

# filtered = [x for x in line1 for y in line2 if x in y]


filtered = []
for x in line1:
    for y in line2:
        if x in y:
            filtered.append(x)
            break


print(filtered)