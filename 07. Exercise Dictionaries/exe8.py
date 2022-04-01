courses = dict()

while True:
    command = input()
    if command == 'end':
        break
    command = command.split(' : ')
    course_name = command[0]
    student_name = command[1]
    if course_name not in courses:
        courses[course_name] = []
        courses[course_name].append(student_name)
    else:
        courses[course_name].append(student_name)

for x in courses:
    print(f"{x}: {len(courses[x])}")
    for y in courses[x]:
        print(f'-- {y}')