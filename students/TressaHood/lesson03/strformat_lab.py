#!/usr/bin/env python3

#lesson 03, String formatting exercise

#Task 3: dynamically build format strings
def formatter(in_tuple):
	"""
	Return a formatted string that can take any length of tuple
	:param: in_tuple : the input tuple that gets formatted and returned
	"""

	#first get the length
	length = len(in_tuple)
	form_string = "the {} numbers are: ".format(length) + "{:d}," * (length-1) + "{:d}"
	print(form_string.format(*in_tuple))

#Task 6: aligning strings
def alignment(name, age, cost):
	"""
	Return a formatted row so that the alignment stays the same
	:param: name, age, cost : the inputs for the row that needs alignment
	"""
	return "{:<8}{:>4}{:>12.2f}". format(name, age, cost)

#define the main function
def main():
	"""
	This is the main function that calls the program
	"""

	#Task 1: format a string with numbers
	tup = (2,123.4567, 10000, 1.23e+04)
	forstring = "file_{:03}: {:.2f}, {:.2e}, {:.2e}".format(*tup)
	print(forstring)

	#Task 2: repeat using alternative 
	forstring = f"file_{tup[0]:03}: {tup[1]:.2f}, {tup[2]:.2e}, {tup[3]:.2e}"
	print(forstring)

	#Task 3: dynamically build format strings
	t = (1,2,3)
	formatter(t)
	t = (2,3,5,7,9)
	formatter(t)

	#Task 4: given an element tuple, use string format
	t = (4,30,2017,2,27)
	forstring = f"{t[3]:02} {t[4]:02} {t[2]:02} {t[0]:02} {t[1]:02}"
	print(forstring)

	#Task 5 fstrings!
	l = ["oranges", 1.3, "lemons", 1.1]
	forstring = f"The weight of an {l[0][:-1].upper()} is {l[1]} and the weight of a {l[2][:-1].upper()} is {l[3]}"
	print(forstring)
	forstring = f"The weight of an {l[0][:-1].upper()} is {l[1] * 1.2} and the weight of a {l[2][:-1].upper()} is {l[3] *1.2}"
	print(forstring)

	#Task 6 algining the rows/columns
	print()
	print("Task 6")
	print("{:<8}{:>4}{:>12}". format("Name", "Age", "Cost"))
	print(alignment("Amy", 32, 37485))
	print(alignment("Sarah", 3, 255.33))
	print(alignment("Erin", 32, 1))

#call the main function
main()
