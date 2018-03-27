for num in range(1:101):
    str = ('')
    if not num % 3:
        str = 'Fizz'
    if not num % 5:
        str += 'Buzz'
    if str == '':
        print(num)
    else:
        print(str)