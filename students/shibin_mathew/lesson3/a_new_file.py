def exchange_first_last(seq):
	#Exchange first and last item
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
	#Every other item removed
	tup_b=()
	str_length = len(seq)
	new_str = ''
	if isinstance(seq, str): #if sequence is a string
		for i, item in enumerate(seq): #loop over the sequence and extract every other value
			if i % 2 == 0: #even value
				new_str+=item #concatenate every other values
		return new_str #return new string
	else:
		for i, item in enumerate(seq):
			if i%2 ==0:
				tup_b = tup_b+(item,)
		return tup_b


def first_last_four_removed(seq):
	#First 4 and last 4 items removed, and then every other item in between
	str_ = ''
	str_ = seq[4:-4]
	str_ = str_[0:-1:2]
	return str_



def elements_reversed(seq):
	#elements reversed
	str_ = ""
	tup = ()
	
	if isinstance(seq, str):
		for i in range(len(seq)-1,-1,-1):
			str_+=seq[i]
		return str_
	else:
		for i in range(len(seq)-1,-1,-1):
			tup = tup + (seq[i],)
		return tup


def new_order(seq):
	#middle third, then last third and first third
	seq_split_3 = len(seq)//3
	first = seq[:seq_split_3] #first split
	second = seq[seq_split_3:seq_split_3*2] #second split
	third = seq[seq_split_3*2:] #third split
	return second+third+first





if __name__ == "__main__":
	a_string = "this is a string"
	a_tuple = (2,54,13,12,5,32,25,5,8,4,6,7,2,3,7,8)
	assert exchange_first_last(a_string) == "ghis is a strint"
	assert exchange_first_last(a_tuple) == (8,54,13,12,5,32,25,5,8,4,6,7,2,3,7,2)
	assert every_other_removed(a_string) == "ti sasrn"
	assert every_other_removed(a_tuple) == (2,13,5,25,8,6,2,7)
	assert first_last_four_removed(a_string) == " sas"
	assert first_last_four_removed(a_tuple) == (5,25,8,6)
	assert elements_reversed(a_string) == "gnirts a si siht"
	assert elements_reversed(a_tuple) == (8,7,3,2,7,6,4,8,5,25,32,5,12,13,54,2)
	assert new_order(a_string) == "is a stringthis "
	assert new_order(a_tuple) == (32,25,5,8,4,6,7,2,3,7,8,2,54,13,12,5)