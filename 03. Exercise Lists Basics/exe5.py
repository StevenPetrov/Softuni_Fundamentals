l = input().split(' ')
number_of_slicing = int(input())

for x in range(number_of_slicing):
    l1 = l[:(len(l)//2)]
    l2 = l[(len(l)//2):]

    l = [c for pair in zip(l1, l2) for c in pair]

print(l)