#!/usr/bin/env python3
# Slicing 
__author___ = "Wieslaw Pucilowski"

### with the first and last items exchanged.
def exchange_first_last(seq):
	return seq[-1:]+seq[1:-1]+seq[:1]
	
### with every other item removed.
def every_other(seq):
	return seq[::2]

### with the first 4 and the last 4 items removed, and then every other item in between.
def rem_first_last_4(seq):
	return seq[4:-4:2]

### with the elements reversed (just with slicing).
def reverse_order(seq):
	return seq[::-1]

### with the middle third, then last third, then the first third in the new order.
def mid_last_first(seq):
	first=len(seq)//3
	second=2*first
	return seq[first:second]+seq[second:]+seq[:first]


def main():
	print("Testing slicing functions...")
	#Testing 1
	print("Testing exchange_first_last()...")
	a_string = "this is a string"
	a_tuple = (2, 54, 13, 12, 5, 32)
	assert exchange_first_last(a_string) == "ghis is a strint"
	assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

	# Testing 2
	print("Testing every_other()...")
	b_string = "abcdefghij"
	b_tuple = (1,2,3,4,5,6,7,8,9,10,11,12)
	assert every_other(b_string) == "acegi"
	assert every_other(b_tuple) == (1,3,5,7,9,11)

	# Testing 3
	print("Testing rem_first_last_4()...")
	c_string="aBcDeFgHiJkLmNoPrSqVwXyZ"
	c_tuple=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
	c1_tuple=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
	assert rem_first_last_4(c_string) == "egikmorq"
	assert rem_first_last_4(c_tuple) == (5,7,9,11,13,15)
	assert rem_first_last_4(c1_tuple) == (4,6,8,10,12,14,16)

	# Testing 4
	print("Testing reversed()...")
	d_string="abc def ghj"
	d_tuple=(1,2,3,4,5,6,7,8,9,10)
	assert reverse_order(d_string) == "jhg fed cba"
	assert reverse_order(d_tuple) == (10,9,8,7,6,5,4,3,2,1)

	# Testing 5
	print("Testing mid_last_first()...")
	e_tuple=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
	assert mid_last_first(a_string) == "is a stringthis "
	assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
	assert mid_last_first(e_tuple) == (6,7,8,9,10,11,12,13,14,15,16,1,2,3,4,5)

if __name__ == "__main__":
	main()

