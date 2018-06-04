# ------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: Fizz_Buzz.py
# PURPOSE: Manipulating data.
#
# DATE: 05/14/2018
#
# DESCRIPTION: Prints integers 1:100 with exceptions (multiples of 3 replaced
# with string "Fizz" multiples of 5 replaced with "Buzz" multiples of both
# 3 and 5 replaced with "Fizz-buzz".
# ---------------------------------------------------------------------

for i in range(1,101):                # Prints all numbers ending at 100
    if i % 3 == 0:                    # if multiple of 3, check for
        if i % 5 == 0:                # multiple of 5, if true > criteria
            print("Fizz-buzz")
        print("Fizz")                 # if "fizz-buzz" not met, then only first
    elif i % 5 == 0:
        print("Buzz")                 # check for only multiple of 5
    else:
        print(i)                      # all others just print normally
