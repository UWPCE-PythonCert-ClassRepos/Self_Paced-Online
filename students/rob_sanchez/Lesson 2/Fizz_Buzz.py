def FizzBuzz():
    #variables
    num1=3
    num2=5
    range_start=1
    range_end=101

    for i in xrange(range_start,range_end):
        if i%num1==0 and i%num2==0:
            print('FizzBuzz')
        elif i%num1==0:
            print('Fizz')
        elif i%num2==0:
            print('Buzz')
        else:
            print(i)
