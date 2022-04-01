d = {}

while True:
    command = input()
    if ':' not in command:
        break

    command = command.split(":")
    name = command[0]
    id = command[1]
    course = command[2]

    if course in d:
        d[course][id] = name
    else:
        d[course] = {}
        d[course][id] = name

command = command.replace("_", " ")

for id in d[command]:
    print(f"{d[command][id]} - {id}")
