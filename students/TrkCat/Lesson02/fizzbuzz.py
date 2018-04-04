for num in range(1,101):
    cur_str = ''
    if not num % 3:
        cur_str = 'Fizz'
    if not num % 5:
        cur_str += 'Buzz'
    if cur_str == '':
        print(num)
    else:
        print(cur_str)