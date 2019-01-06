"""Ian Sahlberg
12/20/2018
Python 210 Assignment 3"""

#Functions

def exchange_first_last(seq):
    """This returns the first and last item of a sequence exchanged"""
    first = seq[-1:]
    mid = seq[1:-1]
    last = seq[:1]
    return print(first + mid + last)

def everyOther(val):
    """This returns a sequence with every other value removed"""
    print(val[::2])

def foursOut(val):
    """This returns a sequence with the first and last 4 values removed and every other value in between"""
    valRange = val[4:-4]
    return print(valRange[::2])


def reverseIt(val):
    """This reutnr s a sequence in reverse order"""
    return print(val[::-1])

#with the middle third, then last third, then the first third in the new order.
def thirds(val):
    """This returns a sequence in the order of the middle third, then last third, then the first third."""
    long = len(val)
    thirds = long//3
    first = val[:thirds]
    mid = val[thirds:(-1*thirds)]
    last = val[-1*thirds:]
    return print(mid+last+first)


#Testing Area


print('Test first_last')
exchange_first_last((1,2,3,4,5))
exchange_first_last(('12345'))
exchange_first_last([1,2,3,4,5])
exchange_first_last([1,2,3])


print('Test every_other')
everyOther('12345678')
everyOther([1,2,3,4,5,6,7,8])
everyOther((1,2,3,4,5,6,7,8))

print('Test foursOut')
foursOut([1,2,3,4,5,6,7,8,9,10,11,12])
foursOut('12345678910111213')
foursOut((1,2,3,4,5,6,7,8,9,10,11,12))

print('Test reverse_it')
reverseIt('1,2,3,4,5')
reverseIt([1,2,3,4,5])
reverseIt((1,2,3,4,5))

print('Test thirds')
thirds([1,2,3,4,5,6,7,8,9])
thirds((1,2,3,4,5,6,7,8,9))
thirds('abcdefghijkl')
thirds('This is a string')
