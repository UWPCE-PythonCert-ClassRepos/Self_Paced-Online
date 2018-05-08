def exchange_first_last(seq):
	""" return seq with first and last elements exchanged"""
	L=len(seq)
	return seq[-1]+seq[1:L-1]+seq[0]

	a_string = "this is a string"
	a_tuple = (1,2,3,4,5,6)

	assert exchange_first_last(a_string) == "ghis is a strint"
	assert exchange_first_last(a_tuple) == (6,2,3,4,5,1)

def rem_odd(seq):
	"""return seq dropping odd elements"""
	return seq[::2]

	a_string = "this is a string"
	a_tuple = (1,2,3,4,5,6)

	assert rem_odd(a_string) == 'ti sasrn'
	assert rem_odd(a_tuple) == (1,3,5)

def rem_ends_odds(seq):
	"""return seq with first and last 4 elements dropped, and dropping odd elements of middle"""
	temp_seq=seq[4:-4]
	return rem_odd(temp_seq)

	a_string = "this is a string"
	a_tuple = (1,2,3,4,5,6,7,8,9,10,11,12)

	assert rem_ends_odds(a_string) == " sas"
	assert rem_ends_odds(a_tuple) == (5,7)

def rev_seq(seq):
	"""return reverse seq"""
	return seq[::-1]

	assert rev_seq("hello")=="olleh"
	assert rev_seq((1,2,3,4,5))==(5,4,3,2,1)

def mid_last_first(seq):
	"""return mid third, then last third, then first third of sequence"""
	if len(seq)%3==2:
		F_L=len(seq)//3+1
	else:
		F_L=len(seq)//3
	return seq[F_L:]+seq[:F_L]

	assert mid_last_first("testing123") =='ting123tes'
	assert mid_last_first("testing1234") == 'ing1234test'
	assert mid_last_first("testing12345") == 'ing12345test'
	assert mid_last_first((1,2,3,4,5))== (3,4,5,1,2)
	