# FizzBuzz.py: implements FizzBuzz excercise for Lesson 2 Assignment

intro = '''UWPCE Python Programming: Lesson 2 Assignment
FizzBuzz: List from 1 to 100, multiples of 3 = "Fizz", multiples of 5 = "Buzz",
multiples of both 3 and 5 = "FizzBuzz"
'''
print(intro)

for x in range(1,101):
    if (x % 3 == 0) & (x % 5 == 0):  # x is a multiple of 3 and 5
        print("FizzBuzz")
    elif x % 3 == 0:  # x is a multiple of 3
        print("Fizz")
    elif x % 5 == 0: # x is a multiple of 5
        print("Buzz")
    else:
        print(x)
