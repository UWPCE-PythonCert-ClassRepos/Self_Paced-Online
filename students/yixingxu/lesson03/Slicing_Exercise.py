def exchange_first_last(seq):
	# the first and last items exchanged
	first = seq[:1]
	mid = seq[1:-1]
	last = seq[-1:]
	a_new_sequence = last + mid + first
	return a_new_sequence

def remove_every_other_item(seq):
	# every other item removed
	a_new_sequence = seq[::2]
	return a_new_sequence
	
def four_letters_exchange_remove(seq):
	#with the first 4 and the last 4 items removed, and then every other item in between
	a_new_sequence = seq[4:-4:2]
	return a_new_sequence	
	
def reverse_seq(seq):
	#with the elements reversed (just with slicing).
	a_new_sequence = seq[-1::-1]
	return a_new_sequence	
	
def mid_last_first(seq):
	# with the middle third, then last third, then the first third in the new order.
	first_third = seq[:len(seq)//3]
	mid_third = seq[len(seq)//3:-len(seq)//3]
	last_third = seq[-len(seq)//3:]
	a_new_sequence = mid_third + last_third + first_third
	return a_new_sequence
	
if __name__ == '__main__':
	a_string = "this is a string"
	a_tuple = (2, 54, 13, 12, 5, 32)
	a_long_tuple = (2, 54, 13, 12, 5, 32,45,12,35,56,10,233,123)
	
	# test the first and last items exchanged
	assert exchange_first_last(a_string) == "ghis is a strint"
	assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

	# test the first and last items exchanged
	assert remove_every_other_item(a_string) == "ti sasrn"
	assert remove_every_other_item(a_tuple) == (2, 13, 5)	
	
	#test with the first 4 and the last 4 items removed, and then every other item in between	
	assert four_letters_exchange_remove(a_string) == " sas"
	assert four_letters_exchange_remove(a_tuple) == ()
	assert four_letters_exchange_remove(a_long_tuple) == (5,45,35)
	
	#test with the elements reversed (just with slicing).
	assert reverse_seq(a_string) == 'gnirts a si siht'
	assert reverse_seq(a_tuple) == (32,5,12,13,54,2)
	
	# test with the middle third, then last third, then the first third in the new order.
	assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
	assert mid_last_first(a_string) == "is a stringthis "
