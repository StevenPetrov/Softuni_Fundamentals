# number = int(input())
#
# number = str(number)
#
# list = []
#
# for x in number:
#     list.append(x)
#
# for x in range(0, len(list)):
#     list[x] = int(list[x])
#
# list.sort(reverse=True)
#
# for x in range(len(list)):
#     print(list[x], end='')

number = list(input())

number.sort(reverse=True)

for x in range(len(number)):
    number[x] = int(number[x])

for x in range(len(number)):
    print(number[x], end='')