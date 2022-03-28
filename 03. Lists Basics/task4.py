list = []
list2 = []
times = int(input())
special_word = input()

for x in range(times):
    list.append(input())

for x in list:
    if special_word in x:
        list2.append(x)

print(list)
print(list2)
