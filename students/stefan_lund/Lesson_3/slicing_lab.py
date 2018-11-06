# python3

# slicing_lab.py


def exchange_first_last(seq):
    """
    seq: expected to be of type string or type tuple
    d:   returns d of the same type as seq
    """
    a = seq[-1:]
    b = seq[1:-1]
    c = seq[:1]
    d = a + b + c
    return d


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
