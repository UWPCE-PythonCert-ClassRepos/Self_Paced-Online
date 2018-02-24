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

if __name__ == '__main__':
    # Create a sample string and a sample sequence, then run the tests
    some_string = 'This is a word salad. It tastes horrible!'
    some_sequence = (534, 'this is hard', 0x51342, 'hello there',
                     ['this', 'is', 'a', 'test'], 543421, 134, 12,
                     20, 86, 543, 9, 8, 7, 6, 5, 'four', 'three', 
                     "two", 'one', 'zero', 'infinity!', -1)
    
    # Run tests on a sample string
    assert first_last_exchange(some_string) == \
            '!his is a word salad. It tastes horribleT'
    assert skip_every_other_item(some_string) == \
            'Ti sawr aa.I atshril!'
    assert remove_leading_and_trailing_4_items_and_take_every_other_item(
            some_string) == ' sawr aa.I atshri'
    assert reverse_items(some_string) == \
            '!elbirroh setsat tI .dalas drow a si sihT'
    assert move_first_third_of_items_to_end(some_string) == \
            'd salad. It tastes horrible!This is a wor'
    
    # Run tests on a sample sequence
    assert first_last_exchange(some_sequence) == (-1, 'this is hard', 
                     0x51342, 'hello there', ['this', 'is', 'a', 'test'], 
                     543421, 134, 12, 20, 86, 543, 9, 8, 7, 6, 5, 'four', 
                     'three', "two", 'one', 'zero', 'infinity!', 534)
    assert skip_every_other_item(some_sequence) == (534, 0x51342,
                     ['this', 'is', 'a', 'test'], 134, 20, 543, 8, 6, 'four',
                     "two", 'zero', -1)
    assert remove_leading_and_trailing_4_items_and_take_every_other_item(
            some_sequence) == (['this', 'is', 'a', 'test'], 134, 20, 543,
                     8, 6, 'four', "two")
    assert reverse_items(some_sequence) == (-1, 'infinity!', 'zero', 'one', 
                     "two", 'three', 'four', 5, 6, 7, 8, 9, 543, 86, 20, 12, 
                     134, 543421, ['this', 'is', 'a', 'test'], 'hello there', 
                     0x51342, 'this is hard', 534)
    assert move_first_third_of_items_to_end(some_sequence) == (12, 20, 86, 543,
                     9, 8, 7, 6, 5, 'four', 'three',  "two", 'one', 'zero',
                     'infinity!', -1, 534, 'this is hard', 0x51342, 
                     'hello there', ['this', 'is', 'a', 'test'], 543421, 134)