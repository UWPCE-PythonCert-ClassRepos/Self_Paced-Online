def fizzbuzz():
    for i in range(1,101):
        if i%3==False and i%5==False:
            print('FizzBuzz')
        elif i%3==False:
            print('Fizz')
        elif i%5==False:
            print('Buzz')
        else:
            print(i)
fizzbuzz()