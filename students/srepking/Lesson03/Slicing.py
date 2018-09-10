def first_to_last(x):
    """Pass a sequence to swap first and last entries."""
    new_list = x[-1:] + x[1:-1] + x[0:1]
    return new_list



def remove_every_other(x):
    """Remove every other item in list"""
    new_list = x[0::2]
    return new_list




def four_and_four(x):
    """With the first 4 and the last 4 items removed, and then every other
    item in between"""
    return x[4:-4:2]





def reverse_list(x):
    """Returns the list in reverse order."""
    return x[::-1]



def thirds(x):
    """Creates a list with the middle third and last third, then the first
    third in the new order"""
    third = len(x) // 3
    return x[third:-third] + x[-third:] + x[:third]


a_string="this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

print('Swap first to last')
assert first_to_last(a_string) == 'ghis is a strint'
assert first_to_last(a_tuple) == (32, 54, 13, 12, 5, 2)

print('Remove Every Other')
assert remove_every_other(a_string) == 'ti sasrn'
assert remove_every_other(a_tuple) == (2, 13, 5)

a_string="this is a string"
a_tuple = (2, 54, 13, 12, 5, 32, 64, 100, 95)

print('Trim first four and last four, then return every other')
assert four_and_four(a_string) == ' sas'
assert four_and_four(a_tuple) == (5,)

print('Return the reverse list')
assert reverse_list(a_string) == "gnirts a si siht"
assert reverse_list(a_tuple) == (95, 100, 64, 32, 5, 12, 13, 54, 2)

print('Creates a new list with the middle third, then last third, then the first third in the new order')
assert thirds(a_string) == 'is a stringthis '

assert thirds(a_tuple) == (12, 5, 32, 64, 100, 95, 2, 54, 13)

