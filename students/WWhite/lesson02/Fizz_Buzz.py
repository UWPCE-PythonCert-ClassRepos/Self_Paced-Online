# -------------------------------------#
# Desc: Fizz Buzz Problem - Printing Fizz, Buzz, and FizzBuzz properly in a range of 0 to 100
# Dev: Will White
# Date: 4/1/2018
# ChangeLog: (When,Who,What)
# -------------------------------------#

for i in range(1, 101):   # Loop through the numbers 1 through 100
    if i % 5 == 0 and i % 3 == 0:  # If the remainder of 3 & 5 is 0:
        print("FizzBuzz")  # Print "FizzBuzz"
    elif i % 5 == 0:  # If the remainder of 5 is 0:
        print("Buzz")  # Print "Buzz"
    elif i % 3 == 0:  # If the remainder of 3 is 0:
        print("Fizz")  # Print "Fizz"
    else:  # If none of the the above are true:
        print(i)  # Print the number

