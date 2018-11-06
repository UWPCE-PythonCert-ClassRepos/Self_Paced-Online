from math import ceil

def swap_first_and_last(seq):
    "Return a copy of seq with the first and last elements swapped."
    return seq[-1:] + seq[1:-1] + seq[0:1]
    
def remove_every_other(seq):
    "Return a copy of seq including the first element and every other element."
    return seq[::2]
    
def remove_4_and_everyother(seq):
    """Return a copy of seq with the first and last 4 elements removed, and 
    every other element between that removed."""
    return seq[4:-4:2]
    
def reverse(seq):
    "Return a reversed copy of seq."
    return seq[::-1]

def mid_last_first(seq):
    """Return a copy of seq reordered so that the middle third of seq is 
    first, followed by the last third and the first third."""
    
    #Ensure that the length of each "third" will differ by no greater than one
    #if the length of seq is not divisible by 3
    if len(seq) % 3 == 1:
        cut_index = len(seq)//3
    else:
        cut_index = ceil(len(seq) / 3)
        
    return seq[cut_index:] + seq[:cut_index]

### Begin Testing Segment ###
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = ['my','favorite','pizza','is','hawaiian',"it's",'not','gross']
a_long_tuple = (1,7,4,3,2,8,7,6,9,5,1,4,8,5,0,2,1,3,5)

assert swap_first_and_last(a_string) == "ghis is a strint"
assert swap_first_and_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert swap_first_and_last(a_list) == ['gross','favorite','pizza','is',
                          'hawaiian',"it's",'not','my']

assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2,13,5)
assert remove_every_other(a_list) == ['my','pizza','hawaiian','not']

assert remove_4_and_everyother(a_string) == " sas"
assert remove_4_and_everyother(a_tuple) == ()
assert remove_4_and_everyother(a_list) == []
assert remove_4_and_everyother(a_long_tuple) == (2,7,9,1,8,0)

assert reverse(a_string) == "gnirts a si siht"
assert reverse(a_tuple) == (32,5,12,13,54,2)
assert reverse(a_list) == ['gross','not',"it's",'hawaiian','is','pizza',
              'favorite','my']

assert mid_last_first(a_string) == "is a stringthis "
assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
assert mid_last_first(a_list) == ['is','hawaiian',"it's",'not','gross','my',
                     'favorite','pizza']
        
    