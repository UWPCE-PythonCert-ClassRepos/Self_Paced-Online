def floor(n):
    """Rounds down a number if there is a remainder"""
    res = int(n)
    return res if res == n or n >= 0 else res-1
    
def exchange_first_last(seq):
    """Reverses the first and last letter or number in a tuple or string"""
    seqfirst = seq[0:0]
    seqlast = seq[-1:]
    remainder = seq[1:-1]
    a_new_sequence = seqlast + remainder + seqfirst
    return a_new_sequence

def remove_every_other(seq):
    """Removes every other item in a tuple or string"""
    a_new_sequence = seq[::2]
    return a_new_sequence
   
def remove_four_every_other(seq):
    """Removes the first four and the last four of a tuple or string, and then gives every other"""
    a_new_sequence = seq[4:-4:2]
    return a_new_sequence
   
def reverse(seq):
    """Reverses an input tuple or string"""
    a_new_sequence = seq[::-1]
    return a_new_sequence

def thirds(seq):
    """Divides an input string or tuple into thirds, and arranges the first third to the end"""
    seq1 = seq[0:floor(len(seq)/3)]
    seq2 = seq[floor(len(seq)/3):]
    a_new_sequence = seq2 + seq1
    return a_new_sequence

if __name__ != "__main__": 
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert remove_every_other(a_string) == 'ti sasrn'
    assert remove_every_other(a_tuple) == (2, 13, 5)
    assert remove_four_every_other(a_string) == ' sas'
    assert remove_four_every_other(a_tuple) == ()
    assert reverse(a_string) == 'gnirts a si siht'
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert thirds(a_string) == 'is a stringthis '
    assert thirds(a_tuple) == (13, 12, 5, 32, 2, 54)
