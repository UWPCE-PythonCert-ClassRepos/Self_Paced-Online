## Ian Letourneau
## 4/25/2018
## A script to list numbers and replace all multiples of 3 and/or 5 with various strings

def fizz_buzz():
	"""A function that prints numbers in range 1-100 inclusive. 
	
		If number is divisible by 3, print "Fizz"
		If number is divisible by 5, print "Buzz"
		If number is divisible by both 3 and 5, print "FizzBuzz"""

	for num in range(1,101):
		if not num%3 and not num%5:
			print('FizzBuzz')
		elif not num%3:
			print('Fizz')
		elif not num%5:
			print('Buzz')
		else:
			print(num)

fizz_buzz()
