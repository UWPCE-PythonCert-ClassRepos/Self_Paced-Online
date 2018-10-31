for it in range(1, 101):
    if it % 3 == 0 and it % 5 != 0:
        print('Fizz')
    elif it % 5 == 0 and it % 3 != 0:
        print('Buzz')
    elif it % 5 == 0 and it % 3 == 0:
        print('FizzBuzz')
    else:
        print(it)
