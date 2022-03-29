def calculator(operator, a, b):
    if operator == "multiply":
        return a * b

    if operator == "divide":
        return int(a / b)

    if operator == "add":
        return a + b

    if operator == "subtract":
        return a - b


print(calculator(operator=input(), a=int(input()), b=int(input())))
