#slicing methods by Ross Martin for lesson 3 assignment

def exchange_first_last(seq):
    """exchange first and last elements of a sequence"""
    return seq[-1:] + seq[1:-1] + seq[:1]
    

def remove_every_other(seq):
    """remove every other item from sequence"""
    return seq[::2]

def remove_first_and_last_four(seq):
    """remove the first four and the last four of the sequence, and then every other"""
    return remove_every_other(seq[4:-4])

def reverse_seq(seq):
    """reverse a sequence"""
    return seq[::-1]

def switch_thirds(seq=[]):
    """divide sequence into 3, return second third then last third then first third
       if thirds not equal in size, the last one will contain the extra columns"""
    third = int(len(seq) / 3)
    new_seq = seq[third:third*2] + seq[third*2:] + seq[:third]
    return new_seq


if __name__ == '__main__':
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)

    assert remove_first_and_last_four(a_string) == " sas"
    #assert remove_first_and_last_four(a_string) == " is a st"
    assert remove_first_and_last_four(a_tuple) == ()
 
    assert reverse_seq(a_string) == "gnirts a si siht"
    assert reverse_seq(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert switch_thirds(a_string) == "is a stringthis "
    assert switch_thirds(a_tuple) == (13, 12, 5, 32, 2, 54)

    print("all tests passed")
