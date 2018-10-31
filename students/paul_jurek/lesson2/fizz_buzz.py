"""module to run the fiz_buz excercise
Goal:
Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead."""


def run_fizz_buzz():
	for i in range (1,101):
		if (i%3==0) & (i%5==0):
			print('FizzBuzz')
		elif i%3==0:
			print('Fizz')
		elif i%5==0:
			print('Buzz')
		else:
			print(i)
		
		
run_fizz_buzz()