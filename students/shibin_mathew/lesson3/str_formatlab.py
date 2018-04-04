import decimal
def format_string(tup):
	# Task One: Write a format string
	print(tup[0]) #Debug
	name_length = tup[0]
	if name_length < 10:
		file_name = 'file_00' + str(tup[0])
	elif name_length < 100:
		file_name = 'file_0' + str(tup[0])
	else:
		file_name = 'file_' + str(tup[0]) + ':'
	sec_num = round(tup[1],2)
	third_num = "{:.2E}".format(decimal.Decimal(tup[2]))
	fourth_num = "{:.2E}".format(decimal.Decimal(tup[3]))
	return file_name + ' ' + str(sec_num) + ' ' + str(third_num) + ' ' + str(fourth_num)

def alternate_string(tup):
	# Task Two: alternate type of format using f-strings
	if tup[0] < 10:
		file_name = f'file_00{tup[0]}' # f-string
	elif tup[0] < 100:
		file_name = f'file_0: {tup[0]}' # f-string
	else:
		file_name = f'file_: {tup[0]}' # f-string
	sec_num = round(tup[1],2)
	third_num = "{:.2E}".format(decimal.Decimal(tup[2]))
	fourth_num = "{:.2E}".format(decimal.Decimal(tup[3]))
	return f'{file_name} {sec_num} {third_num} {fourth_num}'


def formatter(tuple):
	# Dynamically Building up Format Strings
	tup_length = len(tuple)
	form_string = "{:d}," * (tup_length - 1) + "{:d}"
	return f'{"the"} {tup_length} {"numbers are:"} {form_string.format(*tuple)}'

def tuple_formatter(tup):
	# Format tuples in a speciic format
	tup_=()
	return "'" + str(f'{tup[3]:02}') + " " + str(f'{tup[4]:02}') + " " + str(f'{tup[2]:02}') + " " + str(f'{tup[0]:02}') + " " + str(f'{tup[1]:02}') + "'"

def taskFive(list):
	# Write an f-string to display the string in a sentence
	first = list[0]
	return f'The weight of an {list[0][0:-1]} is {list[1]} and the weight of a {list[2][0:-1]} is {list[3]}'

def taskSix(listAlignment):
	# Use alignment specifiers to display data in columns
	for i in listAlignment:
		print("{:<10s}{:<10}{:<10}".format(i[0], i[1], i[2]))

def printTuple(tuple1):
	for i in tuple1:
		print("{:<5}".format(i))
	


if __name__ == "__main__":
	tup = (2, 123.4567, 10000, 12345.67)
	tup2 = (1, 2, 3)
	tup3 = (4, 30, 2017, 2, 27)
	list1 = ['oranges', 1.3, 'lemons', 1.1]
	listAlignment = [['Kimberly',28,125.45], ['Matthew', 29, 25], ['Andreck', 19, 1525.36], ['Ginger', 2, 800], ['Mia', 5, 5500]]
	print(format_string(tup))
	print(alternate_string(tup))
	print(formatter(tup2))
	print(tuple_formatter(tup3))
	print(taskFive(list1))
	taskSix(listAlignment)
	printTuple(tup3)

