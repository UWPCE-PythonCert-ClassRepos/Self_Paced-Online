# Lesson02 assignment
__author__ = "Wieslaw Pucilowski"

# symbol global variable definition
v_slash="|"
cross="+"
dash="-"
space=" "

# first task - print grid
def print_h ():
	print(cross,(dash+space)*4,cross, (dash+space)*4,cross)

def print_m_h():
	print(v_slash,(space+space)*4,v_slash, (space+space)*4,v_slash)

def print_4f(f):
	for i in range(4):
		f()

def print_gr():
	print_h ()
	print_4f(print_m_h)
	print_h ()
	print_4f(print_m_h)
	print_h ()

# second task - print_grid(n)

def print_h2(n):
	print(cross,(space+dash)*n,space+cross,(space+dash)*n,space+cross)

def print_m_h2(n):
	print(v_slash,(space+space)*n,space+v_slash, (space+space)*n,space+v_slash)

def print_nf(f,n):
	for i in range(n):
		f(n)

def print_grid(n):
	m = n // 2
	print_h2(m)
	print_nf(print_m_h2,m)
	print_h2(m)
	print_nf(print_m_h2,m)
	print_h2(m)
	
# third task - print_grid2(m,n)

def print_l3(n,s1,s2):
	print(s1, s2*n, end="")
	
def print_line_h_3(m,n,s1,s2):
	for i in range(m):
		print_l3(n,s1,s2)
		print(space, end="")
	print(space+s1)

def module_(m,n):
	print_line_h_3(m,n,cross,space+dash)
	for i in range(n):
		print_line_h_3(m,n,v_slash,space+space)

def print_grid2(m,n):
	for i in range(m):
		module_(m,n)
	print_line_h_3(m,n,cross,space+dash)

# main

def main():
	print("First task:")
	print_gr()
	print()
	
	print("Second task:")
	
	n = input("Provide n arg for print_grid(n): ")
	print_grid(int(n))
	print()
	
	print("Third task:")
	m = input("Provide m arg for print_grid2(m,n): ")
	n = input("Provide n arg for print_grid2(m,n): ")
	print_grid2(int(m),int(n))

if __name__ == "__main__":
	main()