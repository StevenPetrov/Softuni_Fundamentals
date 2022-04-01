exams_pass = {}
final = {}
while True:
    info = input()
    if info == "end of contests":
        break
    info = info.split(":")
    name = info[0]
    password = info[1]
    exams_pass[name] = password

ppl = {}

while True:
    info = input()
    if info == "end of submissions":
        break
    info = info.split("=>")
    contest = info[0]
    password = info[1]
    username = info[2]
    points = int(info[3])

    if contest in exams_pass:
        if password == exams_pass[contest]:
            if username not in ppl:
                ppl[username] = {}
                ppl[username][contest] = points
            else:
                if contest not in ppl[username]:
                    ppl[username][contest] = points
            if ppl[username][contest] < points:
                ppl[username][contest] = points

best_student = ''
best_points = 0

for x in ppl:
    total = sum(ppl[x].values())
    if total > best_points:
        best_points = total
        best_student = x

print(f"Best candidate is {best_student} with total {best_points} points.")
print('Ranking:')

for x in sorted(ppl):
    print(x)
    for y, points in sorted(ppl[x].items(), key=lambda cp: -cp[1]):
        print(f'#  {y} -> {points}')
