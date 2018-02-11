def fizzbuzz(n):
    """Print fizzbuzz starting at 1 and ending at n"""
    for number in range(1, n+1):
        if number % 3 != 0 and number % 5 != 0:
            print(number)
        else:
            if number % 3 == 0:
                print('Fizz', end='')
            if number % 5 == 0:
                print('Buzz', end='')
            print()

            
fizzbuzz(100)