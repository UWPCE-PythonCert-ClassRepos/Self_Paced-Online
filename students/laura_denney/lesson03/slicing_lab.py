#-------------------------------------------------#
# Title: Slicing Lab
# Dev:   LDenney
# Date:  October 10, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 10/10/18, Created File
#-------------------------------------------------#

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [0,1,2,3,4,5,6,7,8]

def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

def remove_every_other(seq):
    return seq[::2]

def remove_firstlastfour_everyother(seq):
    return seq[4:-4:2]

def elements_reverse(seq):
    return seq[::-1]

def mid_last_first(seq):
    third = len(seq)//3
    return seq[third:third*2] + seq[third*2:] + seq[:third]

#testing block
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert mid_last_first(a_string) == "is a stringthis "
assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
assert remove_every_other(a_tuple) == (2,13,5)
assert remove_every_other(a_string) == "ti sasrn"
assert elements_reverse(a_string) == "gnirts a si siht"
assert elements_reverse(a_tuple) == (32,5,12,13,54,2)
assert remove_firstlastfour_everyother(a_string) == " sas"
assert remove_firstlastfour_everyother(a_tuple) == ()