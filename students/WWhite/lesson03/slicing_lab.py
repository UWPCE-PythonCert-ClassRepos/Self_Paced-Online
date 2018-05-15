# -------------------------------------#
# Desc: Slicing Lab
# Dev: Will White
# Date: 5/2/2018
# ChangeLog: (When,Who,What)
# -------------------------------------#


#  Exchange first and last items
def exchange_first_last(seq):
    return seq[-1] + seq[1:-1] + seq[0]


# Remove every other item
def remove_items(seq):
    return seq[::2]


# Remove first 4 and the last 4 items, and then every other item in between
def first_last_four(seq):
    return seq[4:-4:2]


# Reverse the elements (just with slicing)
def reversed_seq(seq):
    return seq[::-1]


# Reorder to the middle third, then last third, then the first third
def seq_in_thirds(seq):
    seq_third = len(seq)//3
    return seq[seq_third:] + seq[:seq_third]


string_a = "winter is coming"
list_a = [0, 2, 4, 6, 8, 10]