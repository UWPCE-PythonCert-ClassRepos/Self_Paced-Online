def remove_every_other(seq):
    return seq[::2]

assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2, 13, 5)


def remove_first_four_last_four_other_between(seq):
    return  seq[4:-4:2]

a_tuple_longer = (2, 54, 13, 3, 6, 2, 18, 12, 5, 32)

assert remove_first_four_last_four_other_between(a_string) == " sas"
assert remove_first_four_last_four_other_between(a_tuple_longer) == (6,)


def reverse_elements(seq):
    return seq[::-1]

assert reverse_elements(a_string) == "gnirts a si siht"
assert reverse_elements(a_tuple) == (32, 5, 12, 13, 54, 2)


def mid_last_first(seq):
    l = len(seq) // 3
    return seq[l:l*2] + seq[l*2:] + seq[:l]

assert mid_last_first(a_string) == "is a stringthis "
assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)