def fizzBuzz():
    """
        This program prints the numbers from 1 to 100 inclusive.
        But for multiples of three print “Fizz” instead of the number.
        For the multiples of five print “Buzz” instead of the number.
        For numbers which are multiples of both three and five print “FizzBuzz” instead.
    """
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
