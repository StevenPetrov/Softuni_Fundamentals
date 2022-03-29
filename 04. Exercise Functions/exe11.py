def loading_bar(number):
    if number == 100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    elif number == 0:
        print('0% [..........]')
        print('Still loading...')
    else:
        dots = int((100 - number)/10)
        percent = int(number / 10)
        print(f'{number}% [{percent*"%"}{dots*"."}]')
        print('Still loading...')

loading_bar(int(input()))