tickets = input().split(', ')
for x in tickets:
    if len(x) == 20:
        half1 = x[0:10]
        half2 = x[10:20]
        is_jackpot = False
        symbol = ''
        count = 0
        for y in range(len(half1)):
            if half1[y] == half2[y] and half1[y] in "'@', '#', '$' '^' ":
                count += 1
            if count == 10:
                is_jackpot = True
        symbol = half1[4]
        if is_jackpot:
            print(f'ticket "{x}" - 10{symbol} Jackpot!')
        elif count > 5:
            print(f'ticket "{x}" - {count}{symbol}')
        elif count < 6:
            print(f'ticket "{x}" - no match')

    else:
        print("invalid ticket")
    count = 0
    is_jackpot = False
    symbol = ''