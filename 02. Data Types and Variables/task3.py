number = int(input())

for x in range(1, number+1):
    tested_sum = 0
    for n in str(x):
        tested_sum += int(n)
    if tested_sum == 5 or tested_sum == 7 or tested_sum == 11:
        print(f'{x} -> True')
    else:
        print(f'{x} -> False')





