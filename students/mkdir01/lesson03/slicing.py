

def exchange_first_last(x):
    return x[-1:] + x[1:-1] + x[:1]


def every_other(x):
    return x[::2]


def mid_every_other(x):
    return x[4:-4:2]


def elements_reversed(x):
    return x[::-1]


def mid_last_first(x):
    return x[int((len(x)) / 3):] + x[:int((len(x)) / 3)]


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert every_other(a_string) == "ti sasrn"
assert every_other(a_tuple) == (2, 13, 5)

assert mid_every_other(a_string) == " sas"
assert mid_every_other(a_tuple) == ()

assert elements_reversed(a_string) == "gnirts a si siht"
assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)

assert mid_last_first(a_string) == "is a stringthis "
assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
