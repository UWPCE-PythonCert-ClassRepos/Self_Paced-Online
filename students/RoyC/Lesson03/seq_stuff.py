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