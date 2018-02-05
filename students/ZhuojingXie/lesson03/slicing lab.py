#with the first and last items exchanged.
def exchange_first_last(seq):
    return  seq[-1:]+seq[1:-1]+seq[:1]

#with every other item removed.
def remove_everyother_item(seq):
    return seq[0::2]

#with the first 4 and the last 4 items removed, and then every other item in between.
def rm4_keep_other(seq):
    return seq[4:-4:2]

#with the elements reversed (just with slicing).
def reverse(seq):
    return seq[::-1]

#with the middle third, then last third, then the first third in the new order.
def re_order(seq):
    return seq[(int(len(seq)/3)):] + seq[:int(len(seq)/3)]

#Following are test all function

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list= [1,2,3,4,5,6,7,8,9,10,11,12]

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert exchange_first_last(a_list) == [12, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]

assert remove_everyother_item(a_string) == "ti sasrn"
assert remove_everyother_item(a_tuple) == (2, 13, 5)
assert remove_everyother_item(a_list) == [1, 3, 5, 7, 9, 11]

assert rm4_keep_other(a_string) == " sas"
assert rm4_keep_other(a_tuple) == ()
assert rm4_keep_other(a_list) == [5, 7]

assert reverse(a_string) == "gnirts a si siht"
assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)
assert reverse(a_list) == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

assert re_order(a_string) == "is a stringthis "
assert re_order(a_tuple) == (13, 12, 5, 32, 2, 54)
assert re_order(a_list) == [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4]
