def swap_first_last(seq):
    """
    Swap the first and last elements in a sequence
    """
    if len(seq)>1:
        return seq[len(seq)-1:len(seq)]+seq[1:len(seq)-1]+seq[0:1]
    return seq

def rm_every_other(seq):
    """
    Return every other element in a sequence
    """
    return seq[0:len(seq):2]

def rm_firstlast4_every_other(seq):
    """
    Remove first and last four elements from sequence, then return every other 
    element in remaining sequence
    """
    seq = seq[4:len(seq)-4]
    return seq[0:len(seq):2]

one_element = [51]
string_a = 'Love Galore'
seq_a = [5,3,1,2,4,6]
tuple_a = 5,3,1,2,4,6
long_seq = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

assert swap_first_last(string_a) == 'eove GalorL'
assert swap_first_last(seq_a) == [6,3,1,2,4,5]
assert swap_first_last(tuple_a)==(6,3,1,2,4,5)
assert swap_first_last(one_element) == one_element

assert rm_every_other(string_a) == 'Lv aoe'
assert rm_every_other(seq_a) == [5,1,4]
assert rm_every_other(tuple_a) == (5,1,4)
assert rm_every_other(one_element) == [51]

assert rm_firstlast4_every_other(string_a)==' a'
assert rm_firstlast4_every_other(seq_a) == []
assert rm_firstlast4_every_other(tuple_a) == ()
assert rm_firstlast4_every_other(one_element) == []
assert rm_firstlast4_every_other(long_seq)
