l = input().split(', ')
l =sorted(l)
sorted_l = sorted(l,key= lambda x: -len(x))

print(sorted_l)