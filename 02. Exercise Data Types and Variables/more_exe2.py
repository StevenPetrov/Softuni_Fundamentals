number = int(input())
flag = True

if number > 1:
    for x in range(2, number):
        if (number % x) == 0:
            flag = False
            break

if flag:
    print(flag)
else:
    print(flag)
