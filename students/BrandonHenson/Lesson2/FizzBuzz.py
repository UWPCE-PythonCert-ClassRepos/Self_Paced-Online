'''
Brandon Henson
Python 210
Lesson 2
FizzBuzz
4/1/18
'''

#For loop that iterates from 1 to 100 inclusively and
#prints fizz,buzz,fizzbuzz or the number based on divisibilty.
for i in range (1,101):
#This if statement prints "FizzBuzz" if the number is divisible by both 4 AND 5
        if (i % 3 == 0) and (i % 5 == 0):
                print("FizzBuzz")
#This if statement prints "Fizz" if the number is divisible by 3
        elif (i) % 3 == 0:
                print("Fizz")
#This if statement prints "Buzz" if the number is divisible by 5
        elif (i) % 5 == 0:
                print("Buzz")
        else:
#This prints the number if it is not divisible by 3 or 5 or both
                print (i)


