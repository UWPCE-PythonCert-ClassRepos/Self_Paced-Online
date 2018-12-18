"""Write some functions that take a sequence as an argument, and return a copy of that sequence:

with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in between.
with the elements reversed (just with slicing).
with the middle third, then last third, then the first third in the new order.
NOTE: These should work with ANY sequence – but you can use strings to test, if you like.

Your functions should look like:

def exchange_first_last(seq):
    return a_new_sequence
Tests:
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert mid_last_first(a_string) == "is a stringthis "
assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
Write a test or two like that for each of the above functions."""

def exchange_first_last(seq):
    seqlen = len(seq)
    seqlist = '{},'*seqlen
    #return print(seqlist)

    if isinstance(seq, str):
        return seq[-1]+seq[1:-1]+seq[0]
    else:
        if len(seq) ==3:
           return seq[::-1]

        else:
            return seqlist.format(seq[-1],*seq[1:-1], seq[0])
			


#print(exchange_first_last("hello"))
#print(exchange_first_last((1,2,3,4,5)))
#print(exchange_first_last(('12345')))



def everyOther(val):
    build = ''
    buildElse2 = []
    buildElse = ()
    if isinstance(val, str):
        for item in range(0,len(val),2):
            build += str(val[item])
        return print(build)
    elif isinstance(val,tuple):
        for item in range(0, len(val), 2):
            buildElse += val[item],
        return print(buildElse)

    else:
        for item in range(0, len(val), 2):
            buildElse2.append(val[item])
        return print(buildElse2)


def foursOut(val):
    valRange = val[4:-4]
    actualVal = []
    for item in range(0,len(valRange),2):
        actualVal.append(valRange[item])
    return print(actualVal)

foursOut([1,2,3,4,5,6,7,8,9,10,11,12])
foursOut('12345678910111213')


def reverseIt(val):

    if isinstance(val,str):
        return print(val[::-1])
    #elif /can  slice tuples AND lists?

reverseIt('1,2,3,4,5')


#with the middle third, then last third, then the first third in the new order.
def thirds(val):
    long = len(val)
    thirds = long//3
    first = val[:thirds]
    mid = val[thirds:(-1*thirds)]
    last = val[-1*thirds:]
    return print(mid,last,first)

thirds([1,2,3,4,5,6,7,8,9])
