#Fixx, Buzz no Bang!
print("This routine replaces numbers in a range (1 to n, you select n)")
print ("which are divisible by values (v1, v2) you select.")
print (" call this by entering fibu (v1, v2, n)")

def fibu (a, b, n):
	""" Replace each number divizable by variables a or b  respectivle with """
	""" "Fizz" or "Buzz" or both, in the range of 1 through the variable n."""
	for x in range(n+1):
		if x%a == 0:
			if x%b == 0:
				print ("FizzBuzz")
			else:	
				print ("Fizz")
		else:
			if x%b ==0:
				print ("Buzz")
			else:
				print (x)
fibu (3, 5, 100)