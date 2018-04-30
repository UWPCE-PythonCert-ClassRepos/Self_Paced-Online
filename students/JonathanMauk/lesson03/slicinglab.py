def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

a_string = "abcdef"
a_tuple = (1, 2, 3, 4, 5, 6)

assert exchange_first_last(a_string) == "fbcdea"
assert exchange_first_last(a_tuple) == (6, 2, 3, 4, 5, 1)
