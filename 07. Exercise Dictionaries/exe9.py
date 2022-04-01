d = {}

for x in range(int(input())):
    name = input()
    grade = float(input())
    if name not in d:
        d[name] = []
        d[name].append(grade)
    else:
        d[name].append(grade)

for x in d:
    average_grade = (sum(d[x]) / len(d[x]))
    if average_grade >= 4.50:
        print(f'{x} -> {average_grade:.2f}')
