def range_chars(a, b):
    for x in range(ord(a) + 1, ord(b)):
        print(chr(x), end=' ')


range_chars(input(), input())
