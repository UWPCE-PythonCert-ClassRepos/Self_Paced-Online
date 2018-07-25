'''
Shin Tran
Python 210
Lesson 3 Assignment
'''

# Returns a sequence with the first and last items exchanged
def exchangeFirstLast(sequence):
	length = len(sequence) - 1
	first = sequence[0]
	last = sequence[length]
	mid = sequence[1:length]
	if type(sequence) is tuple:
		return (last,) + mid + (first,)
	else:
		return last + mid + first



# Return a sequence with every other item removed
def removeEveryOther(sequence):
	return sequence[::2]



# Returns a sequence with the first 4 and the last
# 4 items removed, and then every other item in between
def truncateFour(sequence):
	newSeq = sequence[4:-4]
	return removeEveryOther(newSeq)



# Returns a sequence with the elements reversed (just with slicing)
def reverse(sequence):
	return sequence[::-1]



# Returns a sequence with the middle third, then last third,
# then the first third in the new order.
def midLastFirst(sequence):
	third = int(len(sequence)/3)
	firstThird = sequence[:third]
	midLast = sequence[third:]
	if type(sequence) is tuple and (len(firstThird) == 1):
		return midLast + firstThird
	else:
		return midLast + firstThird



