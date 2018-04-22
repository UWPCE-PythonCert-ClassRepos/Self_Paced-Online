'''
    File Name: fizzbuzz.py
    Author: Matt Hudgins
    Date created: 3/31/2018
    Date last modified: 3/31/2018
    Python Version 3.6.4
'''

#This should work
#def fizzbuzz(x): 


x = range(1, 101)

for y in x:
    if y % 3 == 0:
        print('Fizz')
    elif y % 5 == 0:
        print('Buzz')
    elif y % 3 == 0 and y % 5 == 0:
        print('FizzBuzz')
    else:
        print(y)

