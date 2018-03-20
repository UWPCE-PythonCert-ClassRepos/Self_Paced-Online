# Write some functions that take a sequence as an argument, and return a copy of that sequence:

# with the first and last items exchanged.
# with every other item removed.
# with the first 4 and the last 4 items removed, and then every other item in between.
# with the elements reversed (just with slicing).
# with the middle third, then last third, then the first third in the new order.

seq = 10,20,30,40,50,60,70,80,90

def exchange_first_last(seq):
    new_0 = seq[-1:]
    new_last_item = seq[0:1]
    middle_seq = seq[1:-1]
    a_new_seq1 = new_0 + middle_seq + new_last_item
    return a_new_seq1


exchange_first_last(seq)



#def remove_every_other(seq):

 #   return a_new_seq2





#def remove_firstLast4_everyOther(seq):

 #   return a_new_seq3





#def reversed_elements(seq):

#    return a_new_seq4





#def middle_last_first_third(seq):

#    return a_new_seq5