#with the first and last items exchanged.
def ex(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]
#with every other item removed.
def alt_text_removed(seq):
    return seq[::2]
#with the first 4 and the last 4 items removed, and then every other item in between.
def first_last_4(seq):
    return seq[4:-4:2]
#with the elements reversed (just with slicing).
def reversed(seq):
    return seq[::-1]
#with the middle third, then last third, then the first third in the new order.
def thirds(seq):
    # Break the string into first, second and third portiona and then concatenate them
    one_third = round(len(seq)/3)
    two_third = round(2*len(seq)/3)
    return seq[one_third:two_third] + seq[two_third:] + seq[:one_third]