"""
Thomas Horn
Series of functions that take a sequence as an argument and return a copy of
that sequence with various manipulations.
"""

def first_last_exchange(sequence):
    """ Exchanges the first and last items of the sequence. """
    print(f"first_last_exchange {sequence[-1:] + sequence[1:-1] + sequence[:1]}")
    return sequence[-1:] + sequence[1:-1] + sequence[:1]


def every_other_remove(sequence):
    """ Removes ever other items of the sequence, beginning with index 1. """
    print(f"every_other_remove {sequence[::2]}")
    return sequence[::2]

def first_4_last_4_every_other_removed(sequence):
    """ 
    Removes the first and last 4 items and every other item beginning with
    index 1.
    """
    print(f"first_4_last_4_every_other_removed {sequence[4:-4:2]}")
    return sequence[4:-4:2]

def reverse_slice(sequence):
    """ Reverses the elements of the sequence via slicing. """
    print(f"reverse_slice {sequence[::-1]}")
    return sequence[::-1]
    

def middlelast_lastfirst_firstmiddle(sequence):
    """ 
    Moves the first third to the middle third's position, middle third to last
    third, and last third to first third.  Each third should be 
    len(sequence)//3 * Position
    """
    third = len(sequence) // 3
    print(f"crazy mixup {sequence[third*2:] + sequence[:third] + sequence[third:third*2]}")
    return sequence[third*2:] + sequence[:third] + sequence[third:third*2]


if __name__ == "__main__":
    sequence = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(sequence[-4])
    assert first_last_exchange(sequence) == (10, 2, 3, 4, 5, 6, 7, 8, 9, 1)
    assert every_other_remove(sequence) == (1, 3, 5, 7, 9)
    assert first_4_last_4_every_other_removed(sequence) == (5,)  # ','?
    assert reverse_slice(sequence) == (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    assert middlelast_lastfirst_firstmiddle(sequence) == (7, 8, 9, 10, 1, 2, 3, 4, 5, 6)

    

