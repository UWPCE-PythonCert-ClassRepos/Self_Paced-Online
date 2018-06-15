import sys

nums = [1,2,3,4,5,6,7,8,9,10]

#Returns a string with the first and last items exchanged
def exchange_first_last(seq):
    first_item = seq[:1]
    last_item = seq[-1:]
    other_itmes = seq[1:-1]
    new_sequence = last_item + other_itmes + first_item
    return new_sequence
    
