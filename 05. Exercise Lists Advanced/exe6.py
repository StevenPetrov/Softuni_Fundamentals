number_of_electrons = int(input())

def electron_disctibution(electrons):
    output = []
    sum_elec = electrons

    for x in range(1,electrons+1):
        if sum_elec == 0:
            break
        elec = (x**2)*2
        if elec > sum_elec:
            output.append(sum_elec)
            break
        else:
            output.append(elec)
            sum_elec -= elec
    return output


print(electron_disctibution(number_of_electrons))