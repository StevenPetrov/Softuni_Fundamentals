def palindrome_check(a):
    for x in a:
        test = x[::-1]
        if test == x:
            print(True)
        else:
            print(False)


list = input().split(', ')

result = palindrome_check(list)
