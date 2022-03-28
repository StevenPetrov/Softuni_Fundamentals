l1 = list(map(int,input().split(' ')))
l2 = list(map(int,input().split(' ')))
l3 = list(map(int,input().split(' ')))

if l1[0] == 1 and l1[1] == 1 and l1[2] == 1:
    print("First player won")
elif l1[0] == 2 and l1[1] == 2 and l1[2] == 2:
    print("Second player won")
elif l2[0] == 1 and l2[1] == 1 and l2[2] == 1:
    print("First player won")
elif l2[0] == 2 and l2[1] == 2 and l2[2] == 2:
    print("Second player won")
elif l3[0] == 1 and l3[1] == 1 and l3[2] == 1:
    print("First player won")
elif l3[0] == 2 and l3[1] == 2 and l3[2] == 2:
    print("Second player won")

elif l1[0] == 2 and l2[0] == 2 and l3[0] == 2:
    print("Second player won")
elif l1[0] == 1 and l2[0] == 1 and l3[0] == 1:
    print("First player won")
elif l1[1] == 2 and l2[1] == 2 and l3[1] == 2:
    print("Second player won")
elif l1[1] == 1 and l2[1] == 1 and l3[1] == 1:
    print("First player won")
elif l1[2] == 2 and l2[2] == 2 and l3[2] == 2:
    print("Second player won")
elif l1[2] == 1 and l2[2] == 1 and l3[2] == 1:
    print("First player won")

elif l1[0] == 1 and l2[1] == 1 and l3[2] == 1:
    print("First player won")
elif l1[0] == 2 and l2[1] == 2 and l3[2] == 2:
    print("Second player won")

elif l1[2] == 1 and l2[1] == 1 and l3[0] == 1:
    print("First player won")
elif l1[2] == 2 and l2[1] == 2 and l3[0] == 2:
    print("Second player won")

else:
    print("Draw!")



