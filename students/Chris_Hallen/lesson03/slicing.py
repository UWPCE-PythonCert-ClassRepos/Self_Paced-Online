
def exchange_first_last(seq):
    """This function returns a copy of a sequence with the first and last items exchanged"""
    beg = seq[slice(len(seq) - 1, len(seq))]
    mid = seq[slice(1, len(seq) - 1)]
    end = seq[slice(0, 1)]
    return beg + mid + end


#  seq = [1, 2, 3, 4]
#  output = exchange_first_last(seq)  # this function call returns [4, 2, 3, 1]
#  print(output)

#  seq = 'crack'
#  output = exchange_first_last(seq)  # this function call returns 'kracc'
#  print(output)


def remove_every_other(seq):
    """This function returns a copy of a sequence with every other item removed"""
    return seq[slice(0, len(seq), 2)]

#  seq = "Christopher"
#  output = remove_every_other(seq)  # this function call returns 'Crsohr'
#  print(output)


#  seq = [0, 1, 2, 4]
#  output = remove_every_other(seq)  # this function call returns [0, 2]
#  print(output)


def first_4_and_last_4_removed(seq):
    """
        This function returns a copy of a sequence
        with the first 4 and the last 4 items removed, and then every other item in between.
    """
    return (seq[slice(4, len(seq) - 4, 2)])


#  seq = "abcdefghijklmnopq"
#  output = first_4_and_last_4_removed(seq)  # this function call returns 'egikm'
#  print(output)

#  seq = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']
#  output = first_4_and_last_4_removed(seq)  # this function call returns ['e', 'g', 'i', 'k', 'm']
#  print(output)


def reverse_elements(seq):
    """ This function returns a copy of a sequence with the elements reversed (just with slicing) """
    return seq[::-1]

# seq = [0, 1, 2, 3]
# output = reverse_elements(seq) # this function call returns [3, 2, 1, 0]
# print(output)

# seq = 'Christopher'
# output = reverse_elements(seq) # this function call returns 'rehpotsirhC'
# print(output)


def mid3rd_last3rd_1st3rd(seq):
    """
       This function returns a copy of a sequence
       with the middle third, then last third, and the first third in a new order
    """
    length = len(seq)
    one_third = int(length / 3)
    first_third = seq[0:one_third]
    middle_third = seq[one_third:one_third * 2]
    last_third = seq[one_third * 2:]
    return middle_third + last_third + first_third


#  seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#  output = mid3rd_last3rd_1st3rd(seq)  # this function call returns [4, 5, 6, 7, 8, 9, 1, 2, 3]
#  print(output)


#  seq = 'blackjack'
#  output = mid3rd_last3rd_1st3rd(seq)  # this function call returns 'ckjackbla'
#  print(output)
