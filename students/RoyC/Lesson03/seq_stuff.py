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
    
