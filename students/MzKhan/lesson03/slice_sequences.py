'''
    Name: Muhammad Khan
    Date: 02/28/2019
    Assignment03

'''

def exchange_first_last(seq):
    # The method swaps the first and the last item in the given sequence.
    # parm: sequence
    # return : sequence
    return seq[-1:]+seq[1:-1]+seq[:1]

def remove_every_other(seq):
    # The method removes the every other item from the given sequence.
    # parm: sequence
    # return: sequence
    return seq[::2]

def remove_first_last_four_and_between(seq):
    # The method removes the first 4 and the last 4 items from the sequence
    # and also every other item.
    # parm: sequence
    # return: sequence
    return seq[4:-4:2]

def reverse_sequence(seq):
    # The method reverses the sequence.
    ## parm: sequence
    # return: sequence
    return seq[::-1]

def swap_third_third(seq):
    # The method re-orders the sequence as
    # The middle third,
    # The last third
    # The first third
    third = len(seq)//3
    return seq[third:-third]+seq[-third:]+seq[:third]


if __name__ =="__main__":
    # Test the methods above using "assert" statement.
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_list = list(range(10))

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last(a_list) == [9,1,2,3,4,5,6,7,8,0]

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2,13,5)
    assert remove_every_other(a_list) == [0,2,4,6,8]

    assert remove_first_last_four_and_between(a_string) == " sas"
    assert remove_first_last_four_and_between(a_tuple) == ()
    assert remove_first_last_four_and_between(a_list) == [4]

    assert reverse_sequence(a_string) == "gnirts a si siht"
    assert reverse_sequence(a_tuple) == (32,5,12,13,54,2)
    assert reverse_sequence(a_list) == list(range(9,-1,-1))

    assert swap_third_third(a_string) == "is a stringthis "
    assert swap_third_third(a_tuple) == (13,12,5,32,2,54)
    assert swap_third_third(a_list) == [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
