# Write some functions that take a sequence as an argument, and return a copy of that sequence:

# with the first and last items exchanged.
# with every other item removed.
# with the first 4 and the last 4 items removed, and then every other item in between.
# with the elements reversed (just with slicing).
# with the middle third, then last third, then the first third in the new order.

tuple_seq = (10,20,30,40,50,60,70,80,90,100,110,120,130,140,150)
string_seq = "Larger than life Jack Pepsi."

# def exchange_first_last(string_seq):
#     new_0 = string_seq[-1:]
#     new_last_item = string_seq[0:1]
#     middle_seq = string_seq[1:-1]
#     a_new_seq1 = new_0 + middle_seq + new_last_item
#     print(a_new_seq1)
#     return a_new_seq1


# exchange_first_last(string_seq)



# def remove_every_other(tuple_seq):
#     tuple_seq = tuple_seq[1::2]
#     print(tuple_seq)
#     #return a_new_seq2


# remove_every_other(tuple_seq)


def remove_firstLast4_everyOther(string_seq):
    first_last_removed = string_seq[4:-4]
    print(first_last_removed)
    a_new_seq3 = first_last_removed[1::2]
    print(a_new_seq3)
    return a_new_seq3


remove_firstLast4_everyOther(string_seq)



# def reversed_elements(string_seq):
#     a_new_seq4 = string_seq[::-1]
#     print(a_new_seq4)
#     return a_new_seq4


# reversed_elements(string_seq)


#def middle_last_first_third(seq):

#    return a_new_seq5