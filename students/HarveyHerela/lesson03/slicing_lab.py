
# Test sequences
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

# The first and last items exchanged.
def exchange_first_last(seq_a):
    seq_b = seq_a[0:0]
    seq_b += seq_a[-1:len(seq_a)]
    seq_b += seq_a[1:-1]
    seq_b += seq_a[0:1]
    return seq_b
    
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

# Every other item removed.
def remove_every_other(seq_a):
    return seq_a[::2]

assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2, 13, 5)

# First 4 and the last 4 items removed, and then every other item in between.
def remove_four(seq_a):
    return seq_a[4:-4:2]

assert remove_four(a_string) == " sas"
assert remove_four(a_tuple) == ()

# The elements reversed (just with slicing).
def reverse(seq_a):
    return seq_a[::-1]

assert reverse(a_string) == "gnirts a si siht"
assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)

# The middle third, then last third, then the first third in the new order.
def switch_thirds(seq_a):
    third = len(seq_a) // 3
    return seq_a[third:] + seq_a[0:third]

assert switch_thirds(a_string) == "is a stringthis "
assert switch_thirds(a_tuple) == (13, 12, 5, 32, 2, 54)
