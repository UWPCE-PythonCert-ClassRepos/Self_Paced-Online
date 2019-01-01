def exchange_first_last(seq):
    a_new_sequence = seq[-1:]+seq[1:-1]+seq[0:1]
    return a_new_sequence

def every_other(seq):
    a_new_sequence = seq[0::2]
    return a_new_sequence

def middle_every_other(seq):
    a_new_sequence = seq[4:-4:2]
    return a_new_sequence

#def reversed(seq):
    #return a_new_sequence

#def thirds(seq):
    #return a_new_sequence

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert every_other(a_string) == "ti sasrn"
assert every_other(a_tuple) == (2,13,5)
assert middle_every_other(a_string) == " sas"
assert middle_every_other(a_tuple) == ()
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
