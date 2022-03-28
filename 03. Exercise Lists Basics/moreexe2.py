l = input().split(' ')
l = list(map(int,l))

middle = int(len(l)/2)

l2 = l[middle+1:]
l2.reverse()
l1 = l[:middle]

car1 = 0
car2 = 0
for x in l1:
    car1 += x
    if x == 0:
       car1 *= 0.8

for x in l2:
    car2 += x
    if x == 0:
        car2 *= 0.8

if car1 < car2:
    winner = 'left'
    total_time = car1
else:
    winner = 'right'
    total_time = car2

print(f"The winner is {winner} with total time: {total_time:.1f}")