l = input().split(', ')
good_names = []
trigger = False

for x in l:
    if 3 <= len(x) <= 16:
        for y in x:
            if y.isalnum() or y in '_!?.,-':
                pass
            else:
                trigger = True
                break
    else:
        trigger = True

    if not trigger:
        good_names.append(x)
    trigger = False

for x in good_names:
    print(''.join(x))