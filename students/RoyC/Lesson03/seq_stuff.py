def exchange_first_last(seq):
    """
    Return a copy of the given sequence with the first and last arguments swapped
    Argument:
        seq - the sequence to manipulate
    """
    return seq[-1:] + seq[1:-1] + seq[:1]
    
def every_other(seq):
    """
    Return a copy of the given sequence with every other item removed
    Argument:
        seq - the sequence to manipulate
    """
    return seq[::2]
    
def some_from_middle(seq):
    """
    Return a copy of the given sequence with first four, last four, and then every other element removed
    Argument:
        seq - the sequence to manipulate
    """
    return seq[4:-4:2]
    
def reverse(seq):
    """
    Return a reversed copy of the given sequence
    Argument:
        seq - the sequence to reverse
    """
    return seq[::-1]
    
def mid_last_first(seq):
    """
    For a given sequence, return a copy reordered to the middle, last and first third of the original
    Argument:
        seq - the sequence to manipulate
    """
    third_len = len(seq)//3
    return seq[third_len:] + seq[:third_len]
    
if __name__ == "__main__":

    # Some random tests of the sequence methods
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_longer_string = a_string + " " + a_string
    a_longer_tuple = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert every_other(a_string) == "ti sasrn"
    assert every_other(a_tuple) == (2, 13, 5)
    assert some_from_middle(a_string) == " sas"
    assert some_from_middle(a_tuple) == ()
    assert some_from_middle(a_longer_string) == " sasrn hsi  t"
    assert some_from_middle(a_longer_tuple) == (25, 35, 45, 55)
    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert mid_last_first(a_string) == "is a stringthis "
    assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)