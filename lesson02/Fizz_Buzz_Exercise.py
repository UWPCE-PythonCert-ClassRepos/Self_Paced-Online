# ------------------------------------------------- #
# Title: Lesson 2, pt 2/3, Fizz Buzz Exercise
# Dev:   Craig Morton
# Date:  8/14/2018
# Change Log: CraigM, 8/14/2018, Fizz Buzz Exercise
#  ------------------------------------------------ #

# Fizz Buzz Exercise:

# 1> Function containing for loop that prints from 1 to 100
# 2> Conditional if statement to print "Fizz" if value is a multiple of three instead of the number
# 3> Conditional if statement to print "Buzz" if value is a multiple of five instead of the number
# 4> Conditional if statement to print "FizzBuzz" if value is a multiple of both three and five


def fizz_buzz():
    """"""
    for value in range(1, 101):
        if value % 3 == 0 and value % 5 == 0:
            print("FizzBuzz")
        elif value % 3 == 0:
            print("Fizz")
        elif value % 5 == 0:
            print("Buzz")
        else:
            print(value)


fizz_buzz()
