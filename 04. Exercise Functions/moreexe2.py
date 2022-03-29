x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

dif1 = 0
dif2 = 0

dif1 = abs(x1) - abs(x2) + abs(y1) - abs(y2)
dif2 = abs(x2) - abs(x1) + abs(y2) - abs(y1)

if dif1 < dif2:
    print(f"({int(x1)}, {int(y1)})")
else:
    print(f"({int(x2)}, {int(y2)})")