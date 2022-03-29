def sum_odd_even(a):
    odd = 0
    even = 0
    for x in a:
        if int(x) % 2 == 0:
            even += int(x)
        else:
            odd += int(x)
    print(f"Odd sum = {odd}, Even sum = {even}")


sum_odd_even(input())
