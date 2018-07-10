#Description: 
#Author: Andy Kwok
#Last Updated: 07/09/2018
#ChangeLog: 
#			v1.0 - Initialization

#test inputs
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


def exchange_first_last(seq):
    """ Function to exchange the first and last items
    seq: argument to be resequence
    """
    a_new_sequence = seq[-1:] + seq[1:-2] + seq[0:1]
    return a_new_sequence
    
def remove_other(seq):
    """ Function to remove every other item
    seq: argument to be resequence
    """
    a_new_sequence = seq[::2]
    return a_new_sequence
    
def remove_first_last_four(seq):
    """ Function to remove the first and last four items and every other in between
    seq: argument to be resequence
    """
    a_new_sequence = seq[4:-4:2]
    return a_new_sequence    
  
def reverse(seq):
    """ Function to reverse every element
    seq: argument to be resequence
    """
    a_new_sequence = seq[::-1]
    return a_new_sequence    
    
def reorder(seq):
    """ Function to show in sequence in the order of the middle third, last third, first third
    seq: argument to be resequence
    """
    third = int(len(seq)/3)
    a_new_sequence = seq[third:2*third] + seq[-third:] +seq[:third]
    return a_new_sequence