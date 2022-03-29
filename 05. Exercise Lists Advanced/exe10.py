def heart_delivery(info):
    failed = False
    index_count = 0
    counter = 0
    while True:
        command = input()
        command = command.split()
        if command[0] == 'Love!':
            break
        index_count += int(command[1])
        if index_count >= len(houses):
            index_count = 0
        if index_count < len(houses):
            houses[index_count] -= 2
            if houses[index_count] < -1:
                print(f"Place {index_count} already had Valentine's day.")
            if houses[index_count] == 0:
                print(f"Place {index_count} has Valentine's day.")
                houses[index_count] -= 1
    print(f"Cupid's last position was {index_count}.")
    for x in houses:
        if x != 0 and x > -1:
            failed = True
            counter += 1
    if failed:
        print(f"Cupid has failed {counter} places.")
    else:
        print("Mission was successful.")


houses = list(map(int, input().split('@')))
heart_delivery(houses)
