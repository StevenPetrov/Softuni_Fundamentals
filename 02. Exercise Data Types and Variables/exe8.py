group_size = int(input())
days = int(input())

companions_count = group_size
coins = 0

for x in range(1,days+1):
    if x % 10 == 0:
        companions_count -= 2
    if x % 15 == 0:
        companions_count += 5
    coins += 50
    coins -= 2 * companions_count
    if x % 3 == 0:
        coins -= companions_count * 3
    if x % 5 == 0:
        coins += companions_count * 20
        if x % 3 == 0:
            coins -= companions_count * 2

print(f'{companions_count} companions received {int(coins/companions_count)} coins each.')