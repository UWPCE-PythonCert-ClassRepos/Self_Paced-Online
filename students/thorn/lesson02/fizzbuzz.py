'''
Thomas Horn
FizzBuzz:  Prints the numbers 1 through 100, substituting "Fizz" for multiples
        of 3 and "Buzz" for multiples of 5.  Multiples of 3 and 5 print
        "FizzBuzz".
'''


def fizz_buzz():
    """ Loops from 1 to 100 checking for above conditions. """
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizozBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)

fizz_buzz()
