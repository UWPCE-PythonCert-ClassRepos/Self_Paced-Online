
# PART ONE
verticle = "+ - + - +"
horizontal = "|   |   |"

print (verticle + "\n" + horizontal + "\n" + verticle + "\n" + horizontal + "\n" + verticle)



# PART TWO
#The assignment shows 4 on each side for 8, and 7 on each side for 15.
#therefore, if it's an odd number, I remove one.
def print_grid(n):
	if n % 2 == 0:
		cap = "+ " 
		bar = "| "
		sp = " "
		h = cap + "- " * int(n/2)
		v = sp * n + bar
		half = int(n/2)
		
		print((h * 2) + cap, end=' ')
		print(("\n" + (bar + (v *2)))*half)
		print((h * 2) + cap, end=' ')
		print(("\n" + (bar + (v *2)))*half)
		print((h * 2) + cap, end=' ')
		print("\n")
	else:
		n = n-1
		print_grid(n)

print_grid(15)



# PART THREE
def print_grid(rc, s):  #Rows\columns and size(length)
	cap = "+ " 
	bar = "| "
	sp = " "

	h = cap + "- " * s
	v = (sp * 2) * s + bar
	
	across= ("\n" + h * rc + cap)
	down= ("\n" + bar + v * rc) 

	print ((across + (down * rc)) * rc)
	print (h * rc + cap)

print_grid(3,4)


# Extra Credit -- Let's let the user decide!
def print_grid(rc, s):  #Rows\columns and size(length)
	cap = "+ " 
	bar = "| "
	sp = " "

	h = cap + "- " * s
	v = (sp * 2) * s + bar
	
	across= ("\n" + h * rc + cap)
	down= ("\n" + bar + v * rc) 

	print ((across + (down * rc)) * rc)
	print (h * rc + cap)

# try 100 , 100  :-)
a = int(input("How many rows and columns ya want...?:  "))
b = int(input("How much spacing ya want...?:  "))
print_grid(a, b)


