l =input().split(' ')
count = int(input())
l1 = []
for x in l:
    l1.append(int(x))
llast = []
for x in l:
    llast.append(int(x))
l = llast

l1.sort()
l1.reverse()


l2 = []

for x in range(count):
    l2.append(l1[-1])
    l1.pop()

for x in l2:
    llast.remove(x)
final = []
for x in llast:
    final.append(str(x))

final = ', '.join(final)

print(final)

# copy_nums = list(map(int, l))