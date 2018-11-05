#Lesson3 - Slicing lab exercise

def exchange_first_last(seq):
    return seq[-1:] + (seq[1 : len(seq) - 1]) + seq[:1]
#----------------------------

def every_other_removed(seq):
    return seq[0 : len(seq) : 2]
#-----------------------------

def crop4_every_other(seq):
    #with the first 4 and the last 4 items removed, and then every other item in between.
    return every_other_removed( seq[4:][:-4] )
#------------------------------------------

def reverse(seq):
    return seq[::-1]
#----------------------------------------

def front_third_to_back(seq):
    return  seq[len(seq) // 3 : ] + seq[ : len(seq) // 3]
#----------------------------------------

a_string = 'abcdefghijklmnopqrstuvwxyz'
a_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
assert exchange_first_last(a_string) == 'zbcdefghijklmnopqrstuvwxya'
assert exchange_first_last(a_tuple) == (15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0)
assert every_other_removed(a_string) == 'acegikmoqsuwy'
assert every_other_removed(a_tuple) == (0, 2, 4, 6, 8, 10, 12, 14)
assert crop4_every_other(a_string)  == 'egikmoqsu'
assert crop4_every_other(a_tuple)  == (4, 6, 8, 10)
assert reverse(a_string) == 'zyxwvutsrqponmlkjihgfedcba'
assert reverse(a_tuple) == (15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
assert front_third_to_back(a_string)  == 'ijklmnopqrstuvwxyzabcdefgh'
assert front_third_to_back(a_tuple) == (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4)
