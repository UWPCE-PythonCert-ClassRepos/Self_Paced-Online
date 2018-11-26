# series function - compute fibonacci and lucas series

def fibonacci(n):
	count = 3
	fibvaln1 = 1
	fibvaln2 = 0
	nextval = fibvaln1 + fibvaln2
	while count < 50:
		if count == n:
			print("The ", n," fibonacci series value is: ", nextval)
		#print("fibvaln1 = ", fibvaln1, "fibvaln2 = ", fibvaln2, "nextval = ", nextval)
		# add fibvaln1 and fibvaln2 for next number in series 
		fibvaln2 = fibvaln1
		fibvaln1 = nextval
		nextval = fibvaln1 + fibvaln2
		count += 1
	
def lucas(n):
	count = 3
	lucvaln1 = 1
	lucvaln2 = 2
	nextval = lucvaln1 + lucvaln2
	while count < 50:
		if count == n:
			print("The ", n," lucas series value is: ", nextval)
		#print("lucvaln1 = ", lucvaln1, "fibvaln2 = ", lucvaln2, "nextval = ", nextval)
		# add lucvaln1 and lucvaln2 for next number in series 
		lucvaln2 = lucvaln1
		lucvaln1 = nextval
		nextval = lucvaln1 + lucvaln2
		count += 1

#def sum_series(x, y, z):


fibonacci(5)
lucas(5)

