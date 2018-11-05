for k in range(1,101):
    
    if not((k % 5) or (k % 3)):
        print('FizzBuzz')
    
    elif not(k % 5):
        print('Buzz')
    
    elif not(k % 3):
        print('Fizz')
    
    else:
        print(k)
        