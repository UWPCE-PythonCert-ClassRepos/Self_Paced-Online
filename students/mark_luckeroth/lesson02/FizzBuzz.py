def fizz_buzz(start=1, end=100):
    """prints numbers start to end, inclusive
       replaces multiples of 3 with 'Fizz'
       replaces multiples of 5 with 'Buzz'
       replaces multiples of 15 with 'FizzBuzz'"""
    for i in range(start,end):
        if (i%3 == 0) and (i%5 == 0):
            print('FizzBuzz')
        elif (i%3 == 0):
            print('Fizz')
        elif (i%5 == 0):
            print('Buzz')
        else:
            print(i)

if __name__ == "__main__":
  fizz_buzz()
