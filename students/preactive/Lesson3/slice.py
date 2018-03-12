def slicer():
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_arr = ["!", "!", "tide", "pod", "challenge", "is",
             "not", "for", "the", "weak", "!", "!"]
    three_types = (a_string, a_tuple, a_arr)

    for slice_item in three_types:
        first_last(slice_item)
        odd_out(slice_item)
        ambigus_ao_fourth(slice_item)
        slice_reversed(slice_item)
        thirds(slice_item)


def first_last(slicer_input):
    # with the first and last items exchanged
    swapped = slicer_input[-1:] + slicer_input[1:-1] \
              + slicer_input[:1]
    return swapped


def odd_out(slicer_input):
    # with every other item removed
    evens = slicer_input[::2]
    return evens


def ambigus_ao_fourth(slicer_input):
    # with the first 4 and the last 4 items removed,
    # and then every other item in between
    ao_forths = odd_out(slicer_input[4:-4])
    return ao_forths


def slice_reversed(slicer_input):
    # with the elements reversed (just with slicing)
    slicer_reversed = slicer_input[::-1]
    return slicer_reversed


def thirds(seq):
    # with the middle third, then last third, then the
    # first third in the new order
    if len(seq) % 3 == 0:
        seq_len = round(len(seq) / 3)
        seq_complete = seq[seq_len:seq_len * 2] \
            + seq[seq_len * 2:seq_len * 3] \
            + seq[:seq_len]
        return seq_complete
    return "Not able to third"


if __name__ == '__main__':
    slicer()


    def testing():
        a_string = "this is a string"
        a_tuple = (2, 54, 13, 12, 5, 32)
        a_arr = ["!", "!", "tide", "pod", "challenge", "is",
                 "not", "for", "the", "weak", "!", "!"]

        # test Strings
        assert first_last(a_string) == "ghis is a strint", "String Failed"
        assert odd_out(a_string) == "ti sasrn", "String Failed"
        assert ambigus_ao_fourth(a_string) == " sas", "String Failed"
        assert slice_reversed(a_string) == "gnirts a si siht", "String Failed"

        # test Tuples
        assert first_last(a_tuple) == (32, 54, 13, 12, 5, 2), "Tuple Failed"
        assert odd_out(a_tuple) == (2, 13, 5), "Tuple Failed"
        assert ambigus_ao_fourth(a_tuple) == (), "Tuple Failed"
        assert slice_reversed(a_tuple) == (32, 5, 12, 13, 54, 2), "Tuple Failed"
        assert thirds(a_tuple) == (13, 12, 5, 32, 2, 54), "Tuple Failed"

        # test Lists
        assert first_last(a_arr) == ["!", "!", "tide", "pod", "challenge", "is",
                                     "not", "for", "the", "weak", "!", "!"], \
            "List failed"
        assert odd_out(a_arr) == ['!', 'tide', 'challenge', 'not', 'the', '!'], \
            "List failed"
        assert ambigus_ao_fourth(a_arr) == ['challenge', 'not'], "List failed"
        assert slice_reversed(a_arr) == ['!', '!', 'weak', 'the', 'for', 'not',
                                         'is', 'challenge', 'pod', 'tide', '!',
                                         '!'], "List failed"
        assert thirds(a_arr) == ['challenge', 'is', 'not', 'for', 'the',
                                 'weak', '!', '!', '!', '!',
                                 'tide', 'pod'], "List failed"
        return


    testing()
