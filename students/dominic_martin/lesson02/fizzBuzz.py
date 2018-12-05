#!/usr/bin/env Python3

#The following code was designed and written by Dominic Martin for UW's Python 210 course.
#This is a Fizz Buzz program for a Lesson02 assignment.

def fizzBuzz():
	for i in range(1, 101):
		if (i % 3 == 0) and (i % 5 == 0):
			print("Fizz Buzz")
		elif i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0:
			print("Buzz")
		else:
			print(i)

fizzBuzz()