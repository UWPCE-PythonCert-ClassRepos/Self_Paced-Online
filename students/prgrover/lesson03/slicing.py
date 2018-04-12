a_string = "The quick brown fox jumps over the lazy dog"
a_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

def exchange_first_last(n):
    """
    Returns a sequence with the first and last items exchanged.

    Args:
    n:  Required. A sequence.
    """

    return n[-1:] + n[1:-1] + n[:1]

def every_other_item_removed(n):
    """
    Returns a sequence with every other item removed.

    Args:
    n:  Required. A sequence.
    """

    return n[::2]

def the_vitamix(n):
    """
    Returns a sequence with the first 4 and the last 4 items removed, and then every other item in between.

    Args:
    n:  Required. A sequence.
    """

    return n[4:-4:2]

def reverse_elements(n):
    """
    Returns a sequence with the elements reversed (using slicing only).

    Args:
    n:  Required. A sequence.
    """

    return n[::-1]

def the_vitamix2(n):
    """
    Returns a sequence with the middle third, then last third, then the first third in the new order.

    Args:
    n:  Required. A sequence.
    """

    #Assign the value for 1/3 the length of n to x for easier readability. 
    x = int(len(n) / 3)


    return n[x:2*x] + n[2*x:] + n[:x]


#Tests
assert(exchange_first_last(a_tuple)) == (100, 20, 30, 40, 50, 60, 70, 80, 90, 10)

assert(every_other_item_removed(a_string)) == "Teqikbonfxjmsoe h aydg"

assert(the_vitamix(a_string)) == "qikbonfxjmsoe h ay"

assert(reverse_elements(a_tuple)) == (100, 90, 80, 70, 60, 50, 40, 30, 20, 10)

assert(the_vitamix2(a_tuple)) == (40, 50, 60, 70, 80, 90, 100, 10, 20, 30)
