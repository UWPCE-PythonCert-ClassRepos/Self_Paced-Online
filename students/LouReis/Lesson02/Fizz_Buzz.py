# Fizz_Buzz.py
# Fizz Buzz assignment
# Coded by LouReis
# Use % to see if there is a remainder from the division and compare with zero.

def fizz_buzz():
    for x in range(0,101):
        if x % 3 == 0 and x % 5 == 0:
            print ("FizzBuzz")
        elif x % 3 == 0 and x % 5 > 0:
            print ("Fizz")
        elif x % 5 == 0 and x % 3 > 0:
            print ("Buzz")
        else:
            print(x)

fizz_buzz()
