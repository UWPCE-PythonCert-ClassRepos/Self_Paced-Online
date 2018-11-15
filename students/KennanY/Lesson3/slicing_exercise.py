def exchange_first_last(seq):
    '''Swaps first and last char in the sequence'''
    return seq[-1:] + seq[1:-1] + seq[:1]

a_string='I like this'
a_tuple= (2, 54, 13, 12, 5, 12)

print(exchange_first_last(a_string))
assert exchange_first_last(a_string) == "s like thiI"

print(exchange_first_last(a_tuple))
assert exchange_first_last(a_tuple) == (12, 54, 13, 12, 5, 2)

##################################################

def remove_every_other(seq):
    ''' Removes every other item'''

    return seq[::2]

a_string='I want to prove'
a_tuple= (2, 54, 13, 12, 5, 12)

print(remove_every_other(a_string))
assert remove_every_other(a_string) =="Iwn opoe"

print(remove_every_other(a_tuple))== (2, 13, 5)

####################################################
def every_other_removed(seq):
    '''The first 4 and the last 4 items removed, and then every other item in between'''

    return seq[4:-4:2]

a_string='123456789abcdefg'
a_tuple= (4, 14, 43, 22, 15, 47, 33, 495, 88, 34, 55, 90)

print(every_other_removed(a_string))
assert every_other_removed(a_string) =="579b"
print(every_other_removed(a_tuple))
assert every_other_removed(a_tuple) ==(15,33)
####################################################
def elements_reversed(seq):
    """Elements reversed """

    return seq[::-1]

a_string='123456789abcdefg'
a_tuple= (4, 14, 43, 22, 15, 47, 33, 495, 88, 34, 55, 90)
print(elements_reversed(a_string))
print(elements_reversed(a_tuple))

assert elements_reversed(a_string) =="gfedcba987654321"
assert elements_reversed(a_tuple) ==(90, 55, 34, 88, 495, 33, 47, 15, 22, 43, 14, 4)
####################################################
def middle(seq):
    """ The middle third, then last third, then the first third in the new order"""

    """Split the sequence into 3 equal parts"""
    firstthird=round(len(seq)/3)
    secondthird=2*round(len(seq)/3)

    return seq[firstthird:secondthird] + seq[secondthird:]+ seq[:firstthird]

a_string='123456789abcdefg'
a_tuple= (4, 14, 43, 22, 15, 47, 33, 495, 88, 34, 55, 90)

print(middle(a_string))
print(middle(a_tuple))
assert middle(a_string) =="6789abcdefg12345"
assert middle(a_tuple) ==(15, 47, 33, 495, 88, 34, 55, 90, 4, 14, 43, 22)