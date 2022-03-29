l =list(map(int, input().split(', ')))

test_list = []
counter = 0
while True:
    if len(l) == 0:
        break
    counter += 10
    for x in l[-100:]:
        if x <= counter:
            test_list.append(x)
            l.remove(x)

    print(f"Group of {counter}'s: {test_list}")
    test_list = []

