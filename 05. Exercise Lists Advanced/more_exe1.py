ppl = list(map(int, input().split(', ')))
min_wealth = int(input())
ppl.sort()
wealth_checker = False
exit = False
while True:
    if exit == True:
        break
    for x in ppl:
        if x < min_wealth:
            wealth_checker = False
            break
    if wealth_checker:
        print(ppl)
        break
    if not wealth_checker:
        for x in ppl:
            if x < min_wealth:
                index = ppl.index(x)
                ppl[index] += 1
                ppl[-1] -= 1
            if ppl[-1] < min_wealth:
                print('No equal distribution possible')
                exit = True
                break

        wealth_checker = True

