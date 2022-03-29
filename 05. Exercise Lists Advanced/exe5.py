rooms = int(input())

free_chairs_left = 0
error = False
room = 0

for x in range(rooms):
    room += 1
    a = input().split(' ')
    if len(a[0]) >= int(a[1]):
        free_chairs_left += len(a[0]) - int(a[1])
    else:
        print(f"{int(a[1]) - len(a[0])} more chairs needed in room {room}")
        error = True

if not error:
    print(f"Game On, {free_chairs_left} free chairs left")
