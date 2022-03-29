def grades(self):

    if self < 3:
        return 'Fail'
    elif self < 3.5:
        return 'Poor'
    elif self < 4.5:
        return 'Good'
    elif self < 5.5:
        return 'Very Good'
    elif self <= 6:
        return 'Excellent'


print(grades(float(input())))

