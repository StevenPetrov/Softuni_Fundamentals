def min_max_sum(a):
    a = list(map(int, a.split(' ')))
    print(f"The minimum number is {min(a)}")
    print(f"The maximum number is {max(a)}")
    print(f"The sum number is: {sum(a)}")

min_max_sum(input())