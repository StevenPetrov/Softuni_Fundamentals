list = []
filtered_list = []

for x in range(int(input())):
    list.append(int(input()))

command = input()

if command == 'even':
    for x in list:
        if x % 2 == 0:
            filtered_list.append(x)
elif command == 'odd':
    for x in list:
        if x % 2 != 0:
            filtered_list.append(x)
elif command == 'negative':
    for x in list:
        if x < 0:
            filtered_list.append(x)
elif command == 'positive':
    for x in list:
        if x >= 0:
            filtered_list.append(x)
            
print(filtered_list)