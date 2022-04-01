parking_dict = {}


def record_check():
    for x in parking_dict:
        print(f'{x} => {parking_dict[x]}')


def parking_reg(parking_dict, command):
    action = command[0]
    name = command[1]
    if len(command) > 2:
        plate = command[2]
    if action == 'register' and name not in parking_dict:
        parking_dict[name] = plate
        print(f"{name} registered {plate} successfully")
    elif action == 'register' and name in parking_dict:
        print(f"ERROR: already registered with plate number {parking_dict[name]}")

    if action == 'unregister' and name in parking_dict:
        print(f"{name} unregistered successfully")
        del parking_dict[name]
    elif action == 'unregister' and name not in parking_dict:
        print(f"ERROR: user {name} not found")


for x in range(int(input())):
    command = input().split()
    parking_reg(parking_dict, command)

record_check()
