#!/usr/bin/env python3

def exchange_first_last(seq):
    """This function exchanges the first and last items in a sequence."""
    if len(seq) <= 1:
        return seq
    else:
        return seq[-1:] + seq[1:-1] + seq[:1]

def rm_every_other_item(seq):
    """This function returns every other item in a sequence."""
    return seq[::2]

def rm_four_every_other(seq):
    """This function removes the first 4 and last 4 items in a sequence and returns every other item in between."""
    return seq[4:-4:2]

def reverse(seq):
    """This function reverses the order of the items in a sequence."""
    return seq[::-1]

def thirds_reorder(seq):
    """This function moves the first one third of items to the end of the sequence."""
    third = len(seq)//3;
    return seq[third:] + seq[:third]



# Test exchange_first_last on some sequence types including empty sequences
assert exchange_first_last('hello there') == 'eello therh'
assert exchange_first_last('') == ''
assert exchange_first_last('h') == 'h'
assert exchange_first_last('hi') == 'ih'
assert exchange_first_last(('item', 2, 67, 5.0, 4, 0)) == (0, 2, 67, 5.0, 4, 'item')
assert exchange_first_last([5, 7, 8, 9, 0]) == [0, 7, 8, 9, 5]

# Test rm_every_other_item on all sequence types including empty sequences
assert rm_every_other_item('hello there') == 'hlotee'
assert rm_every_other_item('') == ''
assert rm_every_other_item('h') == 'h'
assert rm_every_other_item('hi') == 'h'
assert rm_every_other_item((2, 89, [8, 7, 6], 5, 'hi!', 0)) == (2, [8, 7, 6], 'hi!')
assert rm_every_other_item([5, 7, 8, 9, 0]) == [5, 8, 0]

# Test rm_4_every_other on all sequence types including empty sequences
assert rm_four_every_other('here is a string') == ' sas'
assert rm_four_every_other('short') == ''
assert rm_four_every_other((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) == (5, 7, 9)
assert rm_four_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [5, 7]

# Test reverse on all sequence types including empty sequences
assert reverse('hello') == 'olleh'
assert reverse('h') == 'h'
assert reverse('') == ''
assert reverse(('some', 5, 6, [7, 8])) == ([7, 8], 6, 5, 'some')
assert reverse([3, 2, 1]) == [1, 2, 3]

# Test thirds_reorder on all sequence types including empty sequences
assert thirds_reorder('123456789') == '456789123'
assert thirds_reorder('1') == '1'
assert thirds_reorder('') == ''
assert thirds_reorder((5, 6, 7, 8, 9, 10)) == (7, 8, 9, 10, 5, 6)
assert thirds_reorder([5, 6, 7, 8, 9, 10]) == [7, 8, 9, 10, 5, 6]
