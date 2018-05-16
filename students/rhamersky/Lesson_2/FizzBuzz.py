# Description: This program will print Fizz if the number is divisible by 3,
# Buzz if the number is divisible by 5, and FizzBuzz if the number is divisible by 3 & 5.
# Developer: Ryan Hamersky
# Date: 05/01/2018
# Rev: A - 05/15/2018 add comment to the code.

# -----Presentation Section-----

for num in range(1, 101):
    # Is the number divisible by 3 and 5?
    if num % 3 == 0 & num % 5 == 0:
        print("FizzBuzz")
    # Is the number divisible by 3?
    elif num % 3 == 0:
        print("Fizz")
    # Is the number divisible by 5?
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    num =+ 1


