"""
file containing various slicing exercises
"""

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
states = ['Washington','Oregon', 'California', 'Montana']


def exchange_first_last(seq):
    """with the first and last items exchanged"""
    return seq[-1:] + seq[1:-1] + seq[:1]

assert (exchange_first_last(a_string) == "ghis is a strint"), "failed string test"
assert (exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)),"failed tuple test"
assert (exchange_first_last(states) == ['Montana', 'Oregon', 'California', 'Washington']),"failed list test"

def remove_every_other(seq):
    """skip every other item in a sequence"""
    return (seq[::2])

#print (remove_every_other(states))

assert (remove_every_other(a_string) == "ti sasrn"), "failed string test"
assert (remove_every_other(a_tuple) == (2, 13, 5)),"failed tuple test"
assert (remove_every_other(states) == ['Washington', 'California']),"failed list test"

def remove_4_every_other(seq):
    """first 4 and last 4 items removed, and every other in between"""
    return seq[4:-4:2]

#print (remove_4_every_other(a_string))

assert (remove_4_every_other(a_string) == " sas"), "failed string test"
assert (remove_4_every_other(a_tuple) == ()),"failed tuple test"
assert (remove_4_every_other(states) == []),"failed list test"

def reversed_fn(seq):
    """elements reversed"""
    return seq[::-1]

#print (reversed_fn(states))

assert (reversed_fn(a_string) == "gnirts a si siht"), "failed string test"
assert (reversed_fn(a_tuple) == (32, 5, 12, 13, 54, 2)),"failed tuple test"
assert (reversed_fn(states) == ['Montana', 'California', 'Oregon', 'Washington']),"failed list test"

def third_elem(seq):
    """order: middle third, last third, first third """
    l=len(seq)//3
    return seq[l:2*l]+seq[2*l:]+seq[:l]

#print (third_elem(a_string))

assert (third_elem(a_string) == "is a stringthis "), "failed string test"
assert (third_elem(a_tuple) == (13, 12, 5, 32, 2, 54)),"failed tuple test"
assert (third_elem(states) == ['Oregon', 'California', 'Montana', 'Washington']),"failed list test"

print ('done - no error!')
