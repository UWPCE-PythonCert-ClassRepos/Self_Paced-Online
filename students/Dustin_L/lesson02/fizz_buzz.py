#!/usr/bin/env python3


def fizz_buzz(n):
    """Print all integers from 1 to n inclusive with the following rules:

    * Integers that are multiples of 3: print "Fizz"
    * Integers that are multiples of 5: print "Buzz"
    * Integers that are multiples of both 3 and 5: print "FizzBuzz"
    * Print all other integers

    Args:
        n (int): max value
    """
    for i in range(1, n + 1):
        if (i % 15 == 0):
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


if __name__ == '__main__':
    fizz_buzz(100)