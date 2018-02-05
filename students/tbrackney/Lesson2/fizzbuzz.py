"""
File Name: fizzbuzz.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 2/3/2018
Python Version: 3.6.4
"""

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
