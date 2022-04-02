l = input()
n = []
for x in l:
    n.append(x)

power = 0
for x in range(len(n)):
    if x < len(n):
        if n[x] == '>':
            power += int(n[x+1])
            while True:
                if x + 1 < len(n):
                    if power > 0 and n[x+1] != '>':
                        if x + 1 < len(n):
                            n.pop(x+1)
                            power -= 1
                        else:
                            break
                    else:
                        power = power
                        break
                else:
                    break
    else:
        break


print(''.join(n))