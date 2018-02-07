

for i in range(100):
    message = ''
    if (i+1) % 3 == 0:
        message += 'fizz'
    if (i+1) % 5 == 0:
        message += 'buzz'
    #print('length',len(message))
    if len(message) == 0:
        message = str(i + 1)

    print(message)

