def exchange_first_last(seq):
    print(seq[-1:] + seq[1:-1] + seq[:1])
    return seq[-1:] + seq[1:-1] + seq[:1]

def every_other_removed(seq):
    return seq[::2]

def first_last_four(seq):
    return seq[4:-4:2]

def elements_reversed(seq):
    return seq[::-1]

def first_last_third(seq):
    one_third = len(seq)//3
    return seq[one_third * 2:] + seq[:one_third] + seq[one_third: one_third * 2]


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert every_other_removed(a_string) == "ti sasrn"
assert every_other_removed(a_tuple) == (2,13,5)

assert first_last_four(a_string) == ' sas'
assert first_last_four(a_tuple) == ()

assert elements_reversed(a_string) == "gnirts a si siht"
assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)

assert first_last_third(a_string) == "stringthis is a "
assert first_last_third(a_tuple) == (5, 32, 2, 54, 13, 12)




