print ("This routine prepares a matrix of size you choose.")
w=int(input("Cell width?: "))
d=int(input("Cell depth?: "))
r=int(input("How many rows?: "))
c=int(input("Columns?: "))
def print_grid (w, d, r, c):
	boarder="+" + w*" -"
	line="|" + w*"  "
	print (c*boarder + "+")
	for m in range(r):
		for  n in range(d):
			print (c*line + "|")
		print (c*boarder + "+")
print_grid(w, d, r, c)