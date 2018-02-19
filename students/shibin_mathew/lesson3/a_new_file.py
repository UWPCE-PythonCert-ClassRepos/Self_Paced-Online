def exchange_first_last(seq):
	first = ''
	middle = ''
	last = ''
	tup_a = ()
	if isinstance(seq, str):
		return seq[-1]+seq[1:-1]+seq[0]
	else: 
		first = seq[-1]
		middle = seq[1:-1]
		last = seq[0]
		tup_a =  tup_a +(first,)
		tup_a = tup_a + (middle)
		tup_a = tup_a + (last,)
		return tup_a


def every_other_removed(seq):
	tup_b=()
	str_length = len(seq)
	new_str = ''
	if isinstance(seq, str): #if sequence is a string
		for i, item in enumerate(seq): #loop over the sequence and extract every other value
			if i % 2 != 0: #Odd value
				new_str+=item #concatenate every other values
		return new_str #return new string
	else:
		for i, item in enumerate(seq):
			if i%2 !=0:
				tup_b = tup_b+(item,)
		return tup_b


	#return 




def first_last_four_removed(seq):
	return


def elements_reversed(seq):
	return


def new_order(seq):
	return




if __name__ == "__main__":
	a_string = "this is a string"
	a_tuple = (2,54,13,12,5,32)
	print(exchange_first_last(a_string))
	print(exchange_first_last(a_tuple))
	print(every_other_removed(a_string))
	print(every_other_removed(a_tuple))