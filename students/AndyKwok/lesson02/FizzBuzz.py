#Description: Program that prints out Fizz upon division of 3 and Buzz upon division of 5
#Author: Andy Kwok
#Last Updated: 07/01/2018
#ChangeLog: 
#			v1.0 - Initialization

for n in range(1, 101):
	#prints out Fizz/Buzz/FizzBuzz accordingly by if the value can be divided equally by assigned values 
	if n%3 is 0 and n%5 is 0:
		print('FizzBuzz')
	elif n%3 is 0:
		print('Fizz')
	elif n%5 is 0:
		print('Buzz')
	else:
		print(n)