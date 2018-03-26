def fizzbuzz():
    """
    Prints numbers from 1 to 100 inclusive.
    
    1. For multiples of three print “Fizz” instead of the number.
    2. For the multiples of five print “Buzz” instead of the number.
    3. For numbers which are multiples of both three and five print “FizzBuzz” instead.

    Args: None
    """

    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print ('FizzBuzz')
        elif i % 3 == 0:
            print ('Fizz')
        elif i % 5 == 0:
            print ('Buzz')
        else:
            print (i)

fizzbuzz()