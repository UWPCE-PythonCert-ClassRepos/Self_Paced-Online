test_seq = "this is a string"

def exchange_first_last(seq):
    '''exchange 1st and last of sequence'''
    return seq[-1:]+ seq[1:-1] + seq[:1]

def every_other(seq):
    '''remove every other of sequence starting from zeroth'''
    return seq[::2]

def rm_first4_last4_every_other(seq):
    '''remove first four, last four and every other of remaining'''
    return seq[4:-4:2]

def reverse_sequence(seq):
    '''reverse sequence'''
    return seq[::-1]

def first_third_to_end(seq):
    '''move first third of sequence to the end'''
    return seq[round(len(seq) / 3):] + seq[:round(len(seq) / 3)]


#assertions to test functions
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32, 7, 8, 9, 10, 11, 12)


assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (12, 54, 13, 12, 5, 32, 7, 8, 9, 10, 11, 2)
assert rm_first4_last4_every_other(a_string) == " sas"
assert rm_first4_last4_every_other(a_tuple) == (5, 7)
assert every_other(a_string) == "ti sasrn"
assert every_other(a_tuple) == (2, 13, 5, 7, 9, 11)
assert reverse_sequence(a_string) == "gnirts a si siht"
assert reverse_sequence(a_tuple) == (12, 11, 10, 9, 8, 7, 32, 5, 12, 13, 54, 2)
assert first_third_to_end(a_string) == "is a stringthis "
assert first_third_to_end(a_tuple) == (5, 32, 7, 8, 9, 10, 11, 12, 2, 54, 13, 12)