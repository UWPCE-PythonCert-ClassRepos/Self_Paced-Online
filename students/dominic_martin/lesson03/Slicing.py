#!/usr/bin/env Python 3

'''All this program needs added is an input to allow
the user to type an arbitrary sequence.  

It also needs unit tests for each function.
'''
s = 
s = [29, 36, 27, 19, 9, 8, 7, 6, 5, 18, 33, 78, 45, 22, 3]

def firstLast(s):
	'''	This function exchanges the first and last term of sequence.'''
	print("This is the sequence you entered: \n", s)
	print()
	first = s[0]
	last = s[-1]
	s[0] = last
	s[-1] = first
	print("This is the same sequence with the first \n"
		"and last indices exchanged: \n", s)


def everyOther(s):
	''' This function uses slice and step to delete every other index, 
		starting with 0.'''
	print()
	print("This is the new sequence with every other \n"
		"term removed, starting with the second term: \n", s[::2])


def fourInBet(s):
	''' This function uses slice and step to delete the first and last
		four indices and deletes every other index of the remaining
		sequence. '''
	print()
	print("The original sequence now has the first \n"
		"and last four indices removed.  Every other \n"
		"index is deleted from the remaining sequence: \n", s[4:-4:2])

def revSeq(s):
	''' This function uses slice to reverse the order of sequence.'''
	print()
	print("This is the original sequence in reverse:", s[::-1])

def thirds(s):
	''' This function partitions the sequence into thirds and
		rearranges it in the following order: middle, last, first.''' 
	print()
	first = s[0:5]
	middle = s[5:10]
	end = s[10:15]
	newSeq = middle + end + first
	print("This is the original sequence, divided into thirds \n"
		"and rearranged in the following order: \n"
		" Middle -> Last -> First \n", newSeq)

firstLast(s)
everyOther(s)
fourInBet(s)
revSeq(s)
thirds(s)