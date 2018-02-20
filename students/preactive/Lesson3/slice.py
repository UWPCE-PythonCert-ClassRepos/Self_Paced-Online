def slicer():
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_arr = ["!", "!", "tide", "pod", "challenge", "is",
             "not", "for", "the", "weak", "!", "!"]
    three_types = (a_string, a_tuple, a_arr)

    for slice_item in three_types:
        for_type = type(slice_item)
        first_last(slice_item, for_type)
        odd_out(slice_item, for_type)
        ambigus_ao_fourth(slice_item, for_type)
        reversed(slice_item, for_type)
        thirds(slice_item, for_type)



def first_last(slicer_input, for_type):
    # with the first and last items exchanged
    swapped = slicer_input[-1:] + slicer_input[1:len(slicer_input) - 1] \
              + slicer_input[:1]
    if for_type == "str":
        print("str")
    if for_type == "<class 'tuple'>":
        print("tuple")
    if for_type == "<class 'list'>":
        print("list")
    return swapped


def odd_out(slicer_input, for_type):
    # with every other item removed
    evens = slicer_input[::2]
    # print(evens)
    return evens


def ambigus_ao_fourth(slicer_input, for_type):
    # with the first 4 and the last 4 items removed,
    # and then every other item in between
    # print(odd_out(slicer_input[4:-4]))
    return odd_out(slicer_input[4:-4],None)

def reversed(slicer_input, for_type):
    # with the elements reversed (just with slicing)
    return slicer_input[::-1]


def thirds(s_i, for_type):
    # with the middle third, then last third, then the
    # first third in the new order
    if len(s_i) % 3 == 0:
        L = round(len(s_i) / 3)
        # print(s_i[:L])
        # print(s_i[L:L*2])
        # print(s_i[L*2:L*3])
        return s_i[L:L*2] + s_i[L*2:L*3] + s_i[:L]
    return "Not able to third"




slicer()