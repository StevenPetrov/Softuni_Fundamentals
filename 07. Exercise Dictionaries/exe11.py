force = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    if '|' in command:
        command = command.split(' | ')
        special = '|'
        force_side = command[0]
        force_user = command[1]
    else:
        command = command.split(' -> ')
        special = '->'
        force_side = command[1]
        force_user = command[0]

    if special == '|':
        if force_side not in force and force_user not in force.values():
            force[force_side] = []
            force[force_side].append(force_user)
        elif force_user in force.values():
            pass
        if force_user:
            if force_user:
                for x in force:
                    if force_user in force[x] and force_side != x:
                        force[x].remove(force_user)
                        break

    if special == '->':
        if force_user not in force.values() and force_side not in force:
            force[force_side] = []
            force[force_side].append(force_user)
        elif force_user not in force.values():
            force[force_side].append(force_user)
        if force_user:
            for x in force:
                if force_user in force[x] and force_side != x:
                    force[x].remove(force_user)
                    break
        print(f"{force_user} joins the {force_side} side!")

for x in force:
    if len(force[x]) > 0:
        print(f"Side: {x}, Members: {len(force[x])}")
        for y in force[x]:
            print(f'! {y}')
