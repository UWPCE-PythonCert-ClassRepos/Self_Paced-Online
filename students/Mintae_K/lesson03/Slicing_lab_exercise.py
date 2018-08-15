def exchange_f_l(x):
    #print ("with the first and last items exchanged:",s)
    s = x[-1:] + x[1:-1] + x[0:1]
    return s
#
def every_other(x):
    #print ("with every other item removed:",s)
    s = x[::2]
    return s
    #next
def first4last4(x):
    #print ("first 4, last 4 removed, and every other item in between:",s)
    s = x[4:-4:2]
    return s
#next
def reverse_sort(x):
    #print ("with the elements reversed (just with slicing):",s)
    s = x[::-1]
    return s
    #next
def mid3last3first3(x):
    third = int(len(x)/3)
    s = x[third:-third] + x[-third:] + x[:third]
    return s
    #
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
assert exchange_f_l(a_string) == "ghis is a strint"
assert exchange_f_l(a_tuple) == (32, 54, 13, 12, 5, 2)
assert mid3last3first3(a_string) == "is a stringthis "
assert mid3last3first3(a_tuple) == (13, 12, 5, 32, 2, 54)