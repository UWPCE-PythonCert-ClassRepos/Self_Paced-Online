def first_last_exchange(seq):
    """
    Exchange the first and last items of a sequence.

    :return:  The updated sequence.
    """
    return seq[-1:] + seq[1:-1] + seq[:1]

def skip_every_other_item(seq):
    """
    Skip every other item in a sequence.

    :return:  A sequence containing only the even-numbered position
              values of the input sequence.
    """
    return seq[::2]

def remove_leading_and_trailing_4_items_and_take_every_other_item(seq):
    """
    Strip the first 4 and last 4 items of a sequence, and then skip
    every other item from the remaining items in the sequence.

    :return:  The updated sequence.
    """
    return seq[4:-4:2]

def reverse_items(seq):
    """
    Reverse the ordering of a sequence.

    :return:  The sequence of reversed items.
    """
    return seq[::-1]

def move_first_third_of_items_to_end(seq):
    """
    Create a new sequence with the middle third items of a given 
    sequence at the beginning, followed by the last third items, and
    finally the first third items of the original sequence.

    :return:  The updated sequence.
    """
    x = len(seq) // 3
    return seq[x:] + seq[:x]