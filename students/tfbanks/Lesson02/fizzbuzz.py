# FizzBuzz Exercise by tfbanks


def fizzbuzz(x, y, z):  # Defines a function print Fizz, Buzz, and FizzBuzz
    # x is value 1, y is value 2, z is the max value wanted

    for n in range(1, z + 1):  # n+1 insures the max value (z) is included
        if n % x == 0 and n % y == 0:  # Criteria1: Fizzbuzz will print when n is a multiple of both x and y
            print("FizzBuzz")
        elif n % x == 0:  # Criteria2: Fizz will print when n is a multiple of x where first criteria isn't already met
            print("Fizz")
        elif n % y == 0:  # Criteria3: Buzz will print when n is a multiple of y where first criteria isn't already met
            print("Buzz")
        else:
            print(n)  # prints the value of n when when it is not a multiple of either x or y


fizzbuzz(3, 5, 100)  # Runs the function for x = 3 and y = 5 for values between 1 and 100
