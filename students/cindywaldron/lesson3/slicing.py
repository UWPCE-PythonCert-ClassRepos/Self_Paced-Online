#!/usr/bin/env python3

def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

def remove_every_other(seq):
    return seq[0:len(seq):2]

def remove_first4_last4(seq):
    return seq[4:-4:2]

def reverse(seq):
    return seq[::-1]

def mid_last_first(seq):
    count = len(seq)//3
    return seq[count:-count] + seq[-count:] + seq[:count]

if __name__ == '__main__':
    a_string = "this is a string"
    a_tuple = (2,54,13,12,5,32)
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple)  == (32,54,13,12,5,2)

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13,5)

    assert remove_first4_last4(a_string) == " sas"
    assert remove_first4_last4(a_tuple) == ()

    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(a_tuple) == (32,5,12,13,54,2)

    assert mid_last_first(a_string) == "is a stringthis "
    assert mid_last_first(a_tuple) ==(13,12,5,32,2,54)