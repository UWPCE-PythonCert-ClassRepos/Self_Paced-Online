a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

#with the first and last items exchanged.

def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

#with every other item removed.

def every_other(seq):
	return seq[::2]

assert every_other(a_string) == "ti sasrn"

#with the first 4 and the last 4 items removed, and then every other item in between.

def first_and_last_four_removed(seq):
	return seq[4:-4:2]

assert first_and_last_four_removed("asdfTESTasdf") == "TS"

#with the elements reversed (just with slicing).

def reverse(seq):
	return seq[::-1]

assert reverse("abcdefg") == "gfedcba"

#with the middle third, then last third, then the first third in the new order.

def move_thirds(seq):
	sizeofthird = len(seq) // 3
	return seq[-sizeofthird:] + seq[:sizeofthird] + seq[sizeofthird:-sizeofthird]

assert move_thirds("abcdefghi") == "ghiabcdef"
