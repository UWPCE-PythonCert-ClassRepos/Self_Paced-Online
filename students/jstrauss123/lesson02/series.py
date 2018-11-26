# series function - compute fibonacci and lucas series

def fibonacci(n):
	count = 0
	f0 = 0
	f1 = 1
	fibvaln1 = f0 + f1
	fibvaln2 = f1
	nextval = fibvaln1 + fibvaln2
	while count < 50:
		if count == n:
			print("this is the nth iteration, number is: ", n)
		print("fibvaln1 = ", fibvaln1, "fibvaln2 = ", fibvaln2, "nextval = ", nextval)
		# add fibn1 and fibn2 for next number in series 
		fibvaln2 = fibvaln1
		fibvaln1 = nextval
		nextval = fibvaln1 + fibvaln2
		count += 1
	#	fibval = f0 + f1
	#	nextval = fibval +
	#	print(fibval)
	
#def lucas(n):
	

#def sum_series(x, y, z):



fibonacci(11)
