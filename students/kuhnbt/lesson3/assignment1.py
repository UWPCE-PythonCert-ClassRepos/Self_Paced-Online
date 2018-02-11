def exchange_first_last(seq):
    """Exchange first and last elements of input sequence with 
    length>1"""
    return seq[-1:] + seq[1:-2] + seq[:1]


def remove_every_other(seq):
    """Remove every other sequence element, starting at element 1"""
    return seq[::2]


def rm4_and_every_other(seq):
    """Remove first and last 4 elements, then every other element"""
    return remove_every_other(seq[4:-4])


def reverse_seq(seq):
    """Return reversed sequence"""
    return seq[::-1]


def reorder_by_thirds(seq):
    """Return middle third, then last third, then first third"""
    slice_index = len(seq)//3
    return seq[slice_index:] + seq[:slice_index]