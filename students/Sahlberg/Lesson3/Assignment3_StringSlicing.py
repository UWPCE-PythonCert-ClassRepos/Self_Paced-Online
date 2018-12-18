"""Write some functions that take a sequence as an argument, and return a copy of that sequence:

with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in between.
with the elements reversed (just with slicing).
with the middle third, then last third, then the first third in the new order.
NOTE: These should work with ANY sequence – but you can use strings to test, if you like.

Your functions should look like:

def exchange_first_last(seq):
    return a_new_sequence
Tests:
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert mid_last_first(a_string) == "is a stringthis "
assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
Write a test or two like that for each of the above functions."""

def exchange_first_last(seq):
    seqlen = len(seq)
    seqlist = '{},'*seqlen
    #return print(seqlist)

    if isinstance(seq, str):
        return seq[-1]+seq[1:-1]+seq[0]
    else:
        if len(seq) ==3:
           return seq[::-1]

        else:
            return seqlist.format(seq[-1],*seq[1:-1], seq[0])
