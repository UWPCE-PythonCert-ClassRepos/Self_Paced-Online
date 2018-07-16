'''
Shin Tran
Python 210
Lesson 2 Assignment
'''

# Prints the Fibonacci series up to a given number passed as a parameter
# 0, 1, 1, 2, 3, 5, 8, 13
def fibonacci(n):
	x = 0
	y = 1
	for i in range(3,n):
		z = x + y
		x = y
		y = z
		print(z)


# Prints the Lucas series up to a given number passed as a parameter
# 2, 1, 3, 4, 7, 11, 18, 29, ...
def lucas(n):
	x = 2
	y = 1
	for j in range(3,n):
		z = x + y
		x = y
		y = z
		print(z)
