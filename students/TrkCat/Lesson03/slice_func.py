#Slicing functions for Lesson 3 Slicing Lab Exercise

def exchange_first_last(seq):
    """Return seq with first and last items exchanged"""
    return seq[-1:] + seq[1:-1] + seq[:1]
    
    
def remove_every_other(seq):
    """Return seq with every other item removed"""
    return seq[::2]
    
    
def remove_ends_every_other_mid(seq):
    """Return seq with first 4 & last 4 removed & every other in 
    between
    """
    return seq[4:-4:2]

    
def reverse_seq(seq):
    """Return a reversed seq"""
    return seq[::-1]
    
    
def rearrange_thirds(seq):
    """Return mid third + last third + first third of seq"""
    third_len = len(seq)//3
    return seq[third_len:] + seq[:third_len]
    
    
if __name__ == '__main__':
    a_string = 'this is a string'
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_long = [x for x in range(20)]
    
    assert exchange_first_last(a_string) == 'ghis is a strint'
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    
    assert remove_every_other(a_string) == 'ti sasrn'
    assert remove_every_other(a_tuple) == (2, 13, 5)
    
    assert remove_ends_every_other_mid(a_string) == ' sas'
    assert remove_ends_every_other_mid(a_tuple) == ()
    assert remove_ends_every_other_mid(a_long) == [4, 6, 8, 10, 12, 14]
    
    assert reverse_seq(a_string) == 'gnirts a si siht'
    assert reverse_seq(a_tuple) == (32, 5, 12, 13, 54, 2)
    
    assert rearrange_thirds(a_string) == 'is a stringthis '
    assert rearrange_thirds(a_tuple) == (13, 12, 5, 32, 2, 54)
    
    print('All function tests successful')