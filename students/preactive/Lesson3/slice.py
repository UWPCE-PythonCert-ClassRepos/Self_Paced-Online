def slicer():
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_arr = ["!", "!", "tide", "pod", "challenge", "is",
             "not", "for", "the", "weak", "!", "!"]
    thirds(a_arr)


def first_last(slicer_input):
    # with the first and last items exchanged
    swapped = slicer_input[-1:] + slicer_input[1:len(slicer_input) - 1] \
              + slicer_input[:1]
    return swapped


def odd_out(slicer_input):
    # with every other item removed
    evens = slicer_input[::2]
    # print(evens)
    return evens


def ambigus_ao_fourth(slicer_input):
    # with the first 4 and the last 4 items removed,
    # and then every other item in between
    # print(odd_out(slicer_input[4:-4]))
    return odd_out(slicer_input[4:-4])

def reversed(slicer_input):
    # with the elements reversed (just with slicing)
    return slicer_input[::-1]


def thirds(slicer_input):
    # with the middle third, then last third, then the
    # first third in the new order
    if len(slicer_input) % 3 == 0:
        L = len(slicer_input) / 3
        print(L)




slicer()