def perfect_number_checker(number):
    perfect_num_l = []
    for x in range(1,number+1):
        if number % x == 0:
            perfect_num_l.append(x)
    if sum(perfect_num_l) - number == number:
        print("We have a perfect number!" )
    else:
        print("It's not so perfect.")

perfect_number_checker(int(input()))