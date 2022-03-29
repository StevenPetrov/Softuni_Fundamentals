import math


def factorial_calc(a, b):
    a_fact = math.factorial(a)
    b_fact = math.factorial(b)
    division = a_fact / b_fact
    print(f'{division:.2f}')


factorial_calc(int(input()), int(input()))