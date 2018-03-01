def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]
    
def remove_every_other(seq):
    return seq[0:-1:2]

def remove_first_last_four(seq):
    return seq[4:-4]
    
def reverse_elements(seq):
    return seq[::-1]

def new_order_thirds(seq):
    return seq[len(seq)//3 : len(seq)*2//3] + seq[len(seq)*2//3:] + seq[0:len(seq)//3]
    
    
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2, 13, 5)

assert remove_first_last_four(a_string) == " is a st"
assert remove_first_last_four(a_tuple) == ()

assert reverse_elements(a_string) == "gnirts a si siht"
assert reverse_elements(a_tuple) == (32, 5, 12, 13, 54, 2)

assert new_order_thirds(a_string) == "is a stringthis "
assert new_order_thirds(a_tuple) == (13, 12, 5, 32, 2, 54)