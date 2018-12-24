#!/usr/bin/env python
# coding: utf-8

def exchange_first_last(seq):
    a_new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    return(a_new_sequence)

def mid_last_first(seq):
    if type(seq) is str:
        seq = seq.split()
        ll = len(seq)
        m = round(ll/2) - 1
        a_new_sequence =  seq[m:] + seq[:m]
        a_new_sequence = " ".join(a_new_sequence)
    elif type(seq) is tuple:
        ll = len(seq)
        m = round(ll/2) - 1
        a_new_sequence =  seq[m:] + seq[:m]
    return (a_new_sequence)

a_tuple = (2, 54, 13, 12, 5, 32)
a_string = "this is a string"

exchange_first_last(a_tuple)
mid_last_first(a_tuple)
exchange_first_last(a_string)
mid_last_first(a_string)
