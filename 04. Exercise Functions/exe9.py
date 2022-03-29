def password_checker(word):
    long_condition = False
    letters_digits = True
    two_digits = False

    # checking if the password is between 6 and 11 chars
    if 5 < len(word) < 11:
        long_condition = True

    # checking if the password contain any special symbols
    for y in word:
        if not 47 < ord(y) < 58 and not 64 < ord(y) < 91 and not 96 < ord(y) < 123:
            letters_digits = False
            break

    # checking if the password contain at least 2 numbers
    numbers_counter = 0
    for x in word:
        if 47 < ord(x) < 58:
            numbers_counter += 1
    if numbers_counter >= 2:
        two_digits = True

    if long_condition and letters_digits and two_digits:
        print("Password is valid")
    else:
        if not long_condition:
            print("Password must be between 6 and 10 characters")
        if not letters_digits:
            print("Password must consist only of letters and digits")
        if not two_digits:
            print("Password must have at least 2 digits")


password_checker(input())
