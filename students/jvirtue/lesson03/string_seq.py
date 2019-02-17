#Lesson 3 Assignment 1
#Write functions that slice strings
#Jason Virtue 01/12/2019
#UW Self Paced Python Course

#Generic test cases
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
long_tuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

#Fuction One Exchange first and last character of a string
def exchange_seq(seq):
    first = seq[:1]
    last = seq[-1:]
    middle = seq[1:-1]
    return last + middle + first

#Function to remove every other character from string
def every_other_remove(seq):
    newstring = seq[0::2]
    return (newstring)

#Function to take string between fourth and fourth from last.  Skip every other
def slice_str(seq):
    newstring = seq[4:-4:2]
    return newstring

#Reverse elements
def reverse_str(seq):
    rev_seq = seq[::-1]
    return rev_seq

#Split string into thirds with middle, last and first
def third_string(seq):
    segment=int((len(seq))/3)
    first=seq[:segment]
    middle=seq[segment:-(segment)]
    last=seq[-(segment):]
    new_seq = middle + last + first
    return new_seq

#Test out python code
assert exchange_seq(a_string) == "ghis is a strint"
assert exchange_seq(a_tuple) == (32, 54, 13, 12, 5, 2)
assert every_other_remove(a_string) == "ti sasrn"
assert every_other_remove(a_tuple) == (2,13,5)
assert slice_str(long_tuple) == (5,7,9,11,13,15)
assert reverse_str(a_tuple) == (32,5,12,13,54,2)
assert third_string("Thisisitt") == "sisittThi"