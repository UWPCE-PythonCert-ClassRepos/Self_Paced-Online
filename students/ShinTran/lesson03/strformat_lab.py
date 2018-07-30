'''
Shin Tran
Python 210
Lesson 3 Assignment
'''

# Tuple used for tasks 1 and 2
tuple1 = (2, 123.4567, 10000, 12345.67)

'''
The first element is used to generate a filename that can help with file sorting.
The idea behind the “file_002” is that if you have a bunch of files that you want
to name with numbers that can be sorted, you need to “pad” the numbers with zeros
to get the right sort order.
'''
print("file_{:03d} :   {:.2f}, {:.2E}, {:.2E}".format(tuple1[0],\
 tuple1[1], tuple1[2], tuple1[3]))


'''
Using your results from Task One, repeat the exercise, but this time using an
alternate type of format string (hint: think about alternative ways to use
.format() (keywords anyone?), and also consider f-strings if you’ve not used
them already).
'''
first = "file_{:03d}".format(tuple1[0])
second = "{:.2f}".format(tuple1[1])
third = "{:.2E}".format(tuple1[2])
fourth = "{:.2E}".format(tuple1[3])
print(f"{first} :   {second}, {third}, {fourth}")


# Takes in a tuple as a parameter
# Returns a string based on how many elements are in the tuple
# as well the elements in the tuple
def formatter(in_tuple):
	length = len(in_tuple)
	tupleString = str(in_tuple)[1:-1]
	newString = f"the {length} numbers are: {tupleString}"
	if length == 0:
		newString = "the tuple is blank."
	elif length == 1:
		newString = f"the 1 number is: {tupleString}"
	else:
		newString = f"the {length} numbers are: {tupleString}"
	return newString

'''
# Test cases
tempTuple0 = ()
tempTuple1 = (2,)
tempTuple2 = (2,3,5,7,9)
formatter(tempTuple0)
formatter(tempTuple1)
formatter(tempTuple2)
'''


# Tuple used for task 4
tuple4 = (4, 30, 2017, 2, 27)

# use string formating to print:
# '02 27 2017 04 30'
print("{:02d} {:02d} {:02d} {:02d} {:02d}".format(tuple4[0], tuple4[1],\
 tuple4[2], tuple4[3], tuple4[4]))


# List used for task 5
list5 = ['orange', 1.3, 'lemon', 1.1]

# Write an f-string that will display:
# The weight of an orange is 1.3 and the weight of a lemon is 1.1
string5 = "The weight of an {:s} is {:.1f} and the weight of a {:s} is {:.1f}"
print(string5.format(*list5))
newString5 = f"The weight of an {list5[0].upper()} is {list5[1]*1.2},\
 and the weight of a {list5[2].upper()} is {list5[3]*1.2}"
print(newString5)


'''
Write some Python code to print a table of several rows, each with a name,
an age and a cost. Make sure some of the costs are in the hundreds and
thousands to test your alignment specifiers.
And for an extra task, given a tuple with 10 consecutive numbers, can you
work how to quickly print the tuple in columns that are 5 charaters wide?
It’s easily done on one short line!
'''
list6_1 = ['First', '$99.01', 'Second', '$88.09']
list6_2 = ['First', '$99999.01', 'Second', '$8888.09']
list6_3 = ['First', '$999.01', 'Second', '$8.09']
list6_4 = ['First', '$99.01', 'Second', '$888.09']
print('{:15}{:10}{:15}{:15}'.format(*list6_1))
print('{:15}{:10}{:15}{:15}'.format(*list6_2))
print('{:15}{:10}{:15}{:15}'.format(*list6_3))
print('{:15}{:10}{:15}{:15}'.format(*list6_4))

# Tuple of 10 consecutive numbers
tuple6 = [5,16,21,33,47,59,68,73,84,90]
for x in tuple6:
	print("{:5}".format(x))
