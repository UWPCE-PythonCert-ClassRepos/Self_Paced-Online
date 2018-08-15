def fizzBuzz():
    num = 1
    while num <= 100:
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz') 
        elif num % 5 == 0:
            print('Buzz')
        elif num % 3 == 0:
            print('Fizz')
        else:
            print(num)
        num += 1

fizzBuzz()