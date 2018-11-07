"""
	Author is Antonio. V. Alvillar
	Self-Paced-Online Python 210 UWPCE
	November 6th 2018
"""
#Fizz Buzz problem
def fizzBuzz():
    for i in range(1,101): # 1-100 inclusive
        if (i % 3 == 0 ) and (i % 5 == 0): #if multiple of 3 and 5
            print("FizzBuzz")
        elif (i % 3 == 0): #if multiple of 3 but not 5
            print("Fizz")
        elif (i % 5 == 0): #if multiple of 5 but not 3
            print("Buzz")
        else: #if not multiple of 3 or 5
            print(i)