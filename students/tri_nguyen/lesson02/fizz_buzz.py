# -------------------------------------------#
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  02-Feb-2018
# -------------------------------------------#

# write a program that prints the numbers from 1 to 100
# For multiple of three prints 'Fizz' instead of the numbers
# For multiple of five print 'Buzz' instead of the numbers
# For numbers which are multiple of both three and five print
# 'FizzBuzz' instead

for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print('FizzBuzz')
    elif (number % 3 == 0):
        print('Fizz')
    elif (number % 5 == 0):
        print('Buzz')
    else:
        print(number)
