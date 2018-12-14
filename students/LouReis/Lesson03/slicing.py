# slicing.py
#
#
# Coder: LouReis

def copy_sequence(seq):
    """Return a copy of the sequence entered"""
    return seq

def copy_first_last(seq):
    """Return the first and last items of the sequence entered"""
    return seq[0],seq[-1]

def copy_every_other(seq):
    """Return every other item in the sequence entered"""
    return seq[::2]

def copy_rem_first_4_last_4(seq):
    """Return the remaining every other items after removing first 4 & last 4."""
    return seq[4:-4:2]

def copy_reversed(seq):
    """Return the reverse of the items of the sequence entered"""
    return seq[::-1]

def copy_thirds(seq):
    """Return the middle third, then last third, then the first third in the new order."""
    return seq[len(seq)//3:]+seq[:len(seq)//3:]

a_string = "this is a string"
a_tuple = 2, 54, 13, 12, 5, 32

print ("The ORIGINAL string is: ",copy_sequence(a_string))
print ("The ORIGINAL tuple is: ",copy_sequence(a_tuple))
print ("The first and last characters of the string are: ",copy_first_last(a_string))
print ("The first and last elements of the tuple are: ",copy_first_last(a_tuple))
print ("Every other character in the string is: ",copy_every_other(a_string))
print ("Every other element in the tuple is: ",copy_every_other(a_tuple))
print ("The middle every other characters in the string are: ",copy_rem_first_4_last_4(a_string))
print ("The middle every other elements in the tuple are: ",copy_rem_first_4_last_4(a_tuple))
print ("The reversed string is: ",copy_reversed(a_string))
print ("The reversed elements in the tuple are: ",copy_reversed(a_tuple))
print ("The mid third, last third, first third of the string are: ",copy_thirds(a_string))
print ("The mid third, last third, first third of the elements in the tuple are: ",copy_thirds(a_tuple))
