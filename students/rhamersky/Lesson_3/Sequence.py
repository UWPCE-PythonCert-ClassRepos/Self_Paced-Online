#print(exchange_first_last(a_string))
# Description: This program will allow...........
# Developer: Ryan Hamersky
# Date: 05/06/2018
# Rev: A - 05/15/2018 add comment to the code.

# -----Data Section-----
a_string = "this*is*a*string"
a_tuple = (2, 54, 13, 12, 5, 32)

seq = a_tuple
seq1 = a_string

print(seq)
print(seq1)

# -----Process Section-----
def exchange_first_last(seq):
    '''
    This function exchanges the first and last index.
    :param seq: The seq that is passed into the function.
    :return: Returns the newly created sequence.
    '''
    length = len(seq)  # --> Gets length of sequence.
    a_new_sequence = seq[-1:]+seq[1:length-1]+seq[:1]  # --> Exchanges first and last
    return a_new_sequence

# Tests to see if the function is working properly.
print()  # --> Formatting
print(exchange_first_last(seq))
print(exchange_first_last(seq1))

def remove_every_other_item(seq):
    '''
    This function removes every other item.
    :param seq: The seq that is passed into the function.
    :return:Returns the newly created sequence.
    '''
    length = len(seq)  # --> Gets length of sequence.
    a_new_sequence = seq[0:length:2]  # --> Skips every other element
    return a_new_sequence

# Tests to see if the function is working properly.
print()  # --> Formatting
print(remove_every_other_item(seq))
print(remove_every_other_item(seq1))

def remove_first_four_last_four_every_other_item(seq):
    '''
    This function removes the fist and last for indexes and then every
    other item between the first and last four indexes.
    :param seq: The seq that is passed into the function.
    :return: Returns the newly created sequence.
    '''
    length = len(seq)  # --> Gets length of sequence.
    a_new_sequence = seq[4:length-4:2]
    return a_new_sequence

# Tests to see if the function is working properly.
print()  # --> Formatting
print(remove_first_four_last_four_every_other_item(seq))
print(remove_first_four_last_four_every_other_item(seq1))

def reverse_elements(seq):
    '''
    This function reverses all the elements in the sequence.
    :param seq: The seq that is passed into the function.
    :return: Returns the newly created sequence.
    '''
    a_new_sequence = seq[::-1]  # --> Reverses the sequence.
    return a_new_sequence

# Tests to see if the function is working properly.
print()  # --> Formatting
print(reverse_elements(seq))
print(reverse_elements(seq1))

def third_mix_up(seq):
    '''
    This function rearranges the sequence in the followig order: middle third, last third,
    and finally first third.
    :param seq: The seq that is passed into the function.
    :return: Returns the newly created sequence.
    '''
    length = len(seq)  # --> Gets length of sequence.
    a_new_sequence = seq[length//3:2*length//3]+seq[2*length//3:length]+seq[0:length//3]
    return a_new_sequence

# Tests to see if the function is working properly.
print()  # --> Formatting
print(third_mix_up(seq))
print(third_mix_up(seq1))
