for it in range(1, 101):
    if it % 3 == 0 and it % 6 != 0:
        print('Fizz')
    elif it % 6 == 0:
        print('Buzz')
    else:
        print(it)
