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
    if for_type is str:
        assert swapped == "ghis is a strint", "String Failed"
    if for_type is tuple:
        assert swapped == (32, 54, 13, 12, 5, 2), "Tuple Failed"
    if for_type is list:
        assert swapped == ["!", "!", "tide", "pod", "challenge", "is",
                           "not", "for", "the", "weak", "!", "!"], \
            "List failed"
    return swapped


def odd_out(slicer_input, for_type):
    # with every other item removed
    evens = slicer_input[::2]
    if for_type is str:
        assert evens == "ti sasrn", "String Failed"
    if for_type is tuple:
        assert evens == (2, 13, 5), "Tuple Failed"
    if for_type is list:
        assert evens == ['!', 'tide', 'challenge', 'not', 'the', '!'], \
            "List failed"
    return evens


def ambigus_ao_fourth(slicer_input, for_type):
    # with the first 4 and the last 4 items removed,
    # and then every other item in between
    ao_forths = odd_out(slicer_input[4:-4], None)
    if for_type is str:
        assert ao_forths == " sas", "String Failed"
    if for_type is tuple:
        assert ao_forths == (), "Tuple Failed"
    if for_type is list:
        assert ao_forths == ['challenge', 'not'], "List failed"
    return ao_forths


def reversed(slicer_input, for_type):
    # with the elements reversed (just with slicing)
    slicer_reversed = slicer_input[::-1]
    if for_type is str:
        assert slicer_reversed == "gnirts a si siht", "String Failed"
    if for_type is tuple:
        assert slicer_reversed == (32, 5, 12, 13, 54, 2), "Tuple Failed"
    if for_type is list:
        assert slicer_reversed == ['!', '!', 'weak', 'the', 'for', 'not',
                                   'is', 'challenge', 'pod', 'tide', '!',
                                   '!'], "List failed"
    return slicer_reversed


def thirds(s_i, for_type):
    # with the middle third, then last third, then the
    # first third in the new order
    if len(s_i) % 3 == 0:
        L = round(len(s_i) / 3)
        s_i_complete = s_i[L:L * 2] + s_i[L * 2:L * 3] + s_i[:L]
        if for_type is tuple:
            assert s_i_complete == (13, 12, 5, 32, 2, 54), "Tuple Failed"
        if for_type is list:
            assert s_i_complete == ['challenge', 'is', 'not', 'for', 'the',
                                    'weak', '!', '!', '!', '!',
                                    'tide', 'pod'], "List failed"
        return s_i_complete
    return "Not able to third"


slicer()
