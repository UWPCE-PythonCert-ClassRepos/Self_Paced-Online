def fizzbuzz():
    for x in range(1, 100):
        if (x % 3 == 0) or (x % 5 == 0):
            if (x % 3 == 0) and (x % 5 == 0):
                print('FizzBuzz')
            else:
                if (x % 3 == 0):
                    print('Fizz')
                if (x % 5 == 0):
                    print('Buzz')
        else:
            print(x)