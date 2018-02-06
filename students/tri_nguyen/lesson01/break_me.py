# Four simple functions
# Each function, when called, should cause an exception to happen
# Each function should result in one of the four most common exceptions


def name_error():
	''' this function, when called, will cause NameError exception '''
	
	return name_err

def type_error():
	''' this function, when called, will cause TypeError exception '''
	first_num = 9
	second_num = '8'
	return first_num + second_num
	
def syntax_error(a_number):
	''' this function, when called, will cause SyntaxError exception '''
	if int(a_number) > 0
		return 'greater than 0'
	else:
		return 'it is a negative number.'
		
def att_error():
	''' this function, when called, will cause AttributeError '''
	a = 'this is an example'
	return a.break_me
