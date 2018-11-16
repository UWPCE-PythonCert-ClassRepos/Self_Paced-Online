"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    November 13th 2018
"""

#This function will switch the first and last elements of a sequence
def exchange_first_last(seq):
    new_seq = seq[:]
    if len(seq) == 2: #If the sequence only has two elements (switch them)
        new_seq = seq[1:] + seq[0:1]
    elif len(seq) > 2: #If more than two elements
        temp_seq = seq[1:-1] #Copy the middle elements
        new_seq = seq[-1:] + temp_seq + new_seq[:1] #Switch the ends (keep mid)
    return new_seq

#This function will remove every other element in a sequence by slicing
def every_other_removed(seq):
    new_seq = seq[::2] #Remove every other elements (indicated by the 2)
    return new_seq

"""
This function will remove the first and last four then every other element
and if there is not enough it will just return an empty sequence.
"""
def front_back_every_other(seq):
    removed_ends = seq[4:-4] #remove the first and last four elements.
    new_seq = removed_ends[::2] #Remove every other element that remains.
    return new_seq

#This function will just reverse the sequence given
def reverse(seq):
    new_seq = seq[::-1] #Slicing for reversing elements
    return new_seq

#This function will reorder the elements by thirds (middle/last/first)
def mid_last_first(seq):
    third = int(len(seq) / 3) #Third of the sequence length as an integer.
    third_mid = third * 2 #Used for the later third of the sequence
    first = seq[:third]
    mid = seq[third:third_mid]
    last = seq[third_mid:]
    new_seq = mid + last + first #Adding the sequences in the order intended.
    return new_seq



#Assert statements: Each function will test a string, tuple, and list
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#A limited message will appear if a statement fails. (to reduce line length)
assert exchange_first_last(a_string) == "ghis is a strint", "assert exchange_first_last failed"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2), "assert exchange_first_last failed"
assert exchange_first_last(a_list) == [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "assert exchange_first_last failed"

assert every_other_removed(a_string) == 'ti sasrn', "assert every_other_removed failed"
assert every_other_removed(a_tuple) == (2, 13, 5), "assert every_other_removed failed"
assert every_other_removed(a_list) == [0, 2, 4, 6, 8, 10], "assert every_other_removed failed"

assert front_back_every_other(a_string) == ' sas', "assert front_back_every_other failed"
assert front_back_every_other(a_tuple) == (), "assert front_back_every_other failed"
assert front_back_every_other(a_list) == [4, 6], "assert front_back_every_other failed"

assert reverse(a_string) == 'gnirts a si siht', "assert reverse failed"
assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2), "assert reverse failed"
assert reverse(a_list) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], "assert reverse failed"

assert mid_last_first(a_string) == "is a stringthis ", "assert mid_last_first failed"
assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54), "assert mid_last_first failed"
assert mid_last_first(a_list) == [3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2], "assert mid_last_first failed"