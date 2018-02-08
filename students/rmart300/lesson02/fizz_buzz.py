for i in range(1,101):
    message = ''
    if i % 3 == 0:
        message += 'Fizz'
    if i % 5 == 0:
        message += 'Buzz'
    if len(message) == 0:
        message = str(i)

    print(message)

