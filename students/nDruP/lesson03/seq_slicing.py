def swap_first_last(seq):
    """
    Swap the first and last elements in a sequence
    i.e. [1,2,3,4]->[4,2,3,1]
    """
    if len(seq)>1:
        return seq[len(seq)-1:]+seq[1:len(seq)-1]+seq[:1]
    return seq
    
def rm_every_other(seq):
    """
    Return every other element in a sequence
    i.e. [1,2,3,4]->[1,3]
    """
    return seq[0:len(seq):2]

def rm_firstlast4_every_other(seq):
    """
    Omit first and last four elements from sequence, and return every other 
    element in remaining sequence
    i.e. [0,1,2,3,4,5,6,7,8,9,10,11,12]->[4,6,8]
    """
    return seq[4:len(seq)-4:2]
    

def reverse_seq(seq):
    """
    Reverse a given sequence
    i.e. [1,2,3,4]->[4,3,2,1]
    """
    return seq[::-1]

def rearrange_thirds(seq):
    """
    Moves the first third of sequence to the end, then move the rest of the 
    sequence up.
    i.e. [1,2,3,4,5,6]->[3,4,5,6,1,2]
    """
    return seq[len(seq)//3:]+seq[:len(seq)//3]


one_element = [51]
nothin = []
string_a = 'Love Galore'
seq_a = [5,3,1,2,4,6]
seq_b = [5,3,1,2,4,6,8]
seq_c = [5,3,1,2,4,6,8,0]
tuple_a = 5,3,1,2,4,6
long_seq = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

assert swap_first_last(string_a) == 'eove GalorL'
assert swap_first_last(seq_a) == [6,3,1,2,4,5]
assert swap_first_last(tuple_a)==(6,3,1,2,4,5)
assert(swap_first_last(one_element))
assert(swap_first_last(nothin))

assert rm_every_other(string_a) == 'Lv aoe'
assert rm_every_other(seq_a) == [5,1,4]
assert rm_every_other(tuple_a) == (5,1,4)
assert rm_every_other(one_element) == one_element

assert rm_firstlast4_every_other(string_a)==' a'
assert rm_firstlast4_every_other(seq_a) == []
assert rm_firstlast4_every_other(tuple_a) == ()
assert rm_firstlast4_every_other(one_element) == []
assert rm_firstlast4_every_other(long_seq) == [4,6,8,10,12]

assert reverse_seq(string_a) == 'erolaG evoL'
assert reverse_seq(seq_a) == [6,4,2,1,3,5]
assert reverse_seq(tuple_a) == (6,4,2,1,3,5)
assert reverse_seq(one_element) == one_element

assert rearrange_thirds(seq_a) == [1,2,4,6,5,3]
assert rearrange_thirds(tuple_a) == (1,2,4,6,5,3)
assert rearrange_thirds(one_element)==one_element
