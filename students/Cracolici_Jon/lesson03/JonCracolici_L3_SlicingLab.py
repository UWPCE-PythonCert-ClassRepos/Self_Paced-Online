#Jon Cracolici
#Lesson 03 Slicing Lab
#UW Python Cert
#
def firstlastswitch(n):
    """This function switches the first and last items in a sequence."""
    return (n[-1:]+n[1:-1]+n[:1])
#
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
assert firstlastswitch(a_string) == "ghis is a strint"
assert firstlastswitch(a_tuple) == (32, 54, 13, 12, 5, 2)
#
def everyotherdel(n):
    """This function returns every other item in a given sequence."""
    return(n[::2])
#
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
assert everyotherdel(a_string) == "ti sasrn"
assert everyotherdel(a_tuple) == (2,13,5)
#
def chopfourskips(n):
    """This functions chops the first and last four items and returns every other
    remaining item in a sequence."""
    return(n[4:-4:2])
#
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32, 45, 67, 98, 1, 5, 8)
assert chopfourskips(a_string) == " sas"
assert chopfourskips(a_tuple) == (5, 45)
#
def itemsreversed(n):
    """Returns the given sequence with its items reversed."""
    return(n[::-1])
#
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
assert itemsreversed(a_string) == "gnirts a si siht"
assert itemsreversed(a_tuple) == (32, 5, 12, 13, 54, 2)
#
def thirds(n):
    third = int(len(n)/3)
    first = n[0:third]
    middle = n[third:-third]
    last = n[-third::]
    a= middle + last + first
    return(a)
#
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
assert thirds(a_string) == "is a stringthis "
assert thirds(a_tuple) == (13, 12, 5, 32, 2, 54)
#