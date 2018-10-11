#lesson 03, Slicing Lab exercise



def exchange_first_last(seq):
	"""
	Return a copy of the sequence with the first and last items exchanged
	:param seq: a starting sequence
	"""
	a_new_sequence = seq[-1:len(seq)] + seq[1:-1] + seq[0:1]

	#return it
	return a_new_sequence


def every_other_removed(seq):
	"""
	Return a copy of the sequence with every other element removed
	:param seq: a starting sequence
	"""
	a_new_sequence = seq[::2]

	#return it
	return a_new_sequence

def first_last_other(seq):
	"""
	Return a copy of the sequence with the first 4 and the last 4 items removed, then every other 
	item in between.
	:param seq: a starting sequence
	"""
	a_new_sequence = seq[0:4] + seq[-4:] + seq[4:-4:2] 

	#return it
	return a_new_sequence

def reverse_elements(seq):
	"""
	Return a copy of the sequence with the elements in reverse order
	:param seq: a starting sequence
	"""
	a_new_sequence = seq[::-1]

	#return it
	return a_new_sequence

def mid_last_first(seq):
	"""
	Return a copy of the sequence with the middle third, last third, then first third 
	:param seq: a starting sequence
	"""
	thirds = len(seq)//3
	a_new_sequence = seq[thirds:-thirds] + seq[-thirds:] + seq[:thirds]

	#return it
	return a_new_sequence


#define the main function
def main():
	"""
	This is the main function that calls the program
	"""

	#some starting sequences
	a_string = "this is a string"
	a_tuple = (2, 54, 13, 12, 5, 32)

	#test out that the functions work
	print(exchange_first_last(a_string))	
	print(exchange_first_last(a_tuple))
	print(every_other_removed(a_string))
	print(every_other_removed(a_tuple))
	print(first_last_other(a_string))
	print(first_last_other(a_tuple))
	print(reverse_elements(a_string))
	print(reverse_elements(a_tuple))
	print(mid_last_first(a_string))
	print(mid_last_first(a_tuple))
	assert exchange_first_last(a_string) == "ghis is a strint"
	assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
	assert every_other_removed(a_string) == "ti sasrn"
	assert every_other_removed(a_tuple) == (2,13,5)
	assert first_last_other(a_string) == "thisring sas"
	assert first_last_other(a_tuple) == (2, 54, 13, 12, 13, 12, 5, 32)
	assert reverse_elements(a_string) == "gnirts a si siht"
	assert reverse_elements(a_tuple) == (32, 5, 12, 13, 54, 2)
	assert mid_last_first(a_string) == "is a stringthis "
	assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)



#call the main function
main()
