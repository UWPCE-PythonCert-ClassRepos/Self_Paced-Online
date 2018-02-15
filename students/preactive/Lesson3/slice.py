def slicer():
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_arr = ["tide", "pod", "challenge", "is", "not", "for", "the", "weak"]
    first_last(a_tuple)


def first_last(slicer_input):
    # with the first and last items exchanged
    first = slicer_input[0]
    last = slicer_input[-1]
    swapped = last + slicer_input[1:len(slicer_input) - 1] + first
    return swapped


def odd_out():
    # with every other item removed
    print()


def ambigus_ao_fourth():
    # with the first 4 and the last 4 items removed,
    # and then every other item in between
    print()


def reversed():
    # with the elements reversed (just with slicing)
    print()


def thirds():
    # with the middle third, then last third, then the
    # first third in the new order
    print()




slicer()