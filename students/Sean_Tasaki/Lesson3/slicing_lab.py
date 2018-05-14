"""
Sean Tasaki
5/10/2018
Lesson03.slicing_lab
"""

# exchange first and last items in sequence
def exchanged_first_last(seq):
	first = seq[:1]
	last = seq[-1:]
	middle = seq[1: -1]
	return (last + middle + first)

# remove every other item in sequence
def removed_every_other(seq):
	return (seq[::2])


# remove first 4 and last 4 items, then every other item in between
def first4_last4_removed_every_other(seq):
	return (seq[4:-4:2])


# reverse elements
def reversed_elements(seq):
	return (seq[-1::-1])


# middle third, last thiurd, then first third in new order
def middle_last_first(seq):
	third = len(seq) // 3
	first = seq[:third]
	middle = seq[third:third]
	last = seq[third:]
	return(middle + last + first)

# Tests
a_string = "Stuck Inside of Mobile with the Memphis Blues"
a_tuple = (2, 54, 13, 12, 5, 32)
test_list = (1, 2, 3, 4, 5, 6, 7, 8, 9)
test_list2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
assert exchanged_first_last(a_string) == "stuck Inside of Mobile with the Memphis BlueS"
assert exchanged_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert removed_every_other(test_list) == (1, 3, 5, 7, 9)
assert first4_last4_removed_every_other(test_list2) == (5, 7, 9, 11)
assert first4_last4_removed_every_other(a_string) == "kIsd fMbl ihteMmhsB"
assert middle_last_first(test_list) == (4, 5, 6, 7, 8, 9, 1, 2, 3)
assert reversed_elements(test_list) == (9, 8, 7, 6, 5, 4, 3, 2, 1)

