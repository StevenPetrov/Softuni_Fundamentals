num1 = int(input())
times = int(input())


# l = [x for x in range(num1,(times*num1)+1, num1)]
# print(l)


current_number = 0
l = []
for x in range(times):
    current_number += num1
    l.append(current_number)
print(l)