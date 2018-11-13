## NEIMA SCHAFI, LESSON 3 Assignment - Slicing

def slice1(seq):
    """The function that switches the first and last items exchanged in a sequence"""
    seq2 = seq[-1:] + seq[1:-1] + seq[0:1]
    return seq2

def slice2(seq):
    """The function that removes every other item in a sequence"""
    seq2 = seq[::2]
    return seq2

def slice3(seq):
    """The function which removes first 4 and the last 4 items, and then every other item in between in sequence"""
    seq2 = seq[4:-4]
    seq2 = seq2[::2]
    if len(seq) < 8:
        print("Need to input sequence larger than 8 items or else you will get an empty sequence in return")
    return seq2

def slice4(seq):
    """The function that reverses a sequence"""
    seq2 = seq[::-1]
    return seq2

def slice5(seq):
    """The function that reorders a sequence as such the middle third, then last third, then the first third in the new order."""
    if len(seq) < 3:
        print('function cannot perform with sequences less than 3')
    three = len(seq)//3 ##dividing initial sequence length into thirds
    seq2 = seq[1*three:1*three*2] + seq[1*three*2:] + seq[0:1*three]
    return seq2


####TEST BLOCK
s = "this is a string"
t = (2, 54, 13, 10, 9, 8)
t2 = (2, 54, 13, 10, 9, 8, 67, 80, 90, 45)

##Tests for slice1 function (swapping first and last elements)
assert slice1(s) == "ghis is a strint"
assert slice1(t) == (8, 54, 13, 10, 9, 2)

##Test for slice2 function (remove everyother)
assert slice2(t) == (2, 13, 9)

##Test for slice3 function (remove first/last 4 and then everyother)
assert slice3(t2) == (9,)

##Tests for slice4 function (reversing sequence)
assert slice4(t) == (8, 9, 10, 13, 54, 2)
assert slice4(s) == ("gnirts a si siht")

##Tests for slice5 function (reorders sequence by middle 1/3, last 1/3, first 1/3)
assert slice5(s) == "is a stringthis "
assert slice5(t) == (13, 10, 9, 8, 2, 54)

##END OF ASSIGNMENT
