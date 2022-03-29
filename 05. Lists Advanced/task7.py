happy_l = list(map(int, input().split(' ')))
multiplyer = int(input())

overall = list(map(lambda x: x * multiplyer, happy_l))

happy_count = [x for x in overall if x > sum(overall)/len(overall)]

if len(happy_count) >= len(overall)/2:
    print(f"Score: {len(happy_count)}/{len(overall)}. Employees are happy!")
else:
    print(f"Score: {len(happy_count)}/{len(overall)}. Employees are not happy!")