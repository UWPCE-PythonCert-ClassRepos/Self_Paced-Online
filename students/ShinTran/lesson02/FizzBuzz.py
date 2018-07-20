'''
Shin Tran
Python 210
Lesson 2 Assignment
'''

# Prints all the numbers from 1 through 100 inclusive
# For multiples of 3's, it would print Fizz instead
# For multiples of 5's, it would print Buzz instead
# For multiples of 3's and 5's, it would print FizzBuzz instead
def printFizzBuzz():
	for i in range(1,101):
		if (i % 3 == 0 and i % 5 == 0):
			print('FizzBuzz')
		elif (i % 3 == 0):
			print('Fizz')
		elif (i % 5 == 0):
			print('Buzz')
		else:
			print(i)