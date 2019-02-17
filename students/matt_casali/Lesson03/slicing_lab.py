# test data
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

# with the first and last items exchanged
def first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

assert(first_last(a_string)) == "ghis is a strint"
assert(first_last(a_tuple)) == (32, 54, 13, 12, 5, 2)

# with every other item removed
def every_other(seq):
    return seq[0::2]

assert(every_other(a_string)) == "ti sasrn"
assert(every_other(a_tuple)) == (2, 13, 5)

# with the first 4 and the last 4 items removed, and then every other item in between
def fours_other(seq):
    return seq[4:-4:2]

assert(fours_other(a_string)) == " sas"
assert(fours_other(a_tuple)) == ()

# with the elements reversed (just with slicing)
def reversed(seq):
    return seq[::-1]

assert(reversed(a_string)) == "gnirts a si siht"
assert(reversed(a_tuple)) == (32, 5, 12, 13, 54, 2)

# with the middle third, then last third, then the first third in the new order
def thirds(seq):
    return seq[len(seq) // 3: len(seq) * 2 // 3] + seq[len(seq) * 2 // 3:] + seq[0: len(seq) // 3]

assert(thirds(a_string)) == "is a stringthis "
assert(thirds(a_tuple)) == (13, 12, 5, 32, 2, 54)