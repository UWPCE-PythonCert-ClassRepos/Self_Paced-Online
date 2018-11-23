# python3

# slicing_lab.py:
# with the first and last items exchanged.
# with every other item removed.
# with the first 4 and the last 4 items removed, and then every other
#   item in between.
# with the elements reversed (just with slicing).
# with the middle third, then last third, then the first third in the new order.


def exchange_first_last(seq, n):
    """
        seq: expected to be of type string, list or type tuple
        d:   returns d of the same type as seq
        returns seq with the first and the last n items exchanged
    """

    a = seq[-n:]
    b = seq[n:-n]
    c = seq[:n]
    d = a + b + c

    return d


# a_string = "this is a string"
# a_tuple = (2, 54, 13, 12, 5, 32)
#
# assert exchange_first_last(a_string) == "ghis is a strint"
# assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

def leave_every_nth(seq, n):
    """
        seq: expected to be of type string, list or type tuple
        d:   returns d of the same type as seq
        returns seq with every n item left
            if n is negative order is also reversed
    """
    return seq[::n]


def remove_n_and_leave_every_mth(seq, n, m):
    """
        seq: expected to be of type string, list or type tuple
        d:   returns d of the same type as seq
        returns seq with with the first 'n' and the last 'n' items removed,
            and then every m items in between is left.
    """
    return seq[n:-n:m]


def reverse(seq):
    """
        seq: expected to be of type string, list or type tuple
        d:   returns d of the same type as seq
        return  elements in seq reversed
    """
    return seq[::-1]


def change_slice_order(seq):
    """
    """

    length = len(seq)
    slicelen, r = length // 3, length % 3
    if r == 2:
        slicelen += 1

    first = seq[:slicelen]
    second_and_third = seq[slicelen:]

    return second_and_third + first


if __name__ == '__main__':
    print("\nslicing_lab:\n")

    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    for i in range(1, 5):
        b_string = exchange_first_last(a_string, i)
        b_tuple = exchange_first_last(a_tuple, i)
        print("exchange_first_last(seq, n), n = ", i)
        print("Seq. In:  {}  \nSeq. Out: {}\n".format(a_string, b_string))
        print("Seq. In:  {}  \nSeq. Out: {}\n".format(a_tuple, b_tuple))

    for i in range(1, 5):
        b_string = leave_every_nth(a_string, i)
        b_tuple = leave_every_nth(a_tuple, i)
        print("leave_every_nth(seq, n), n = ", i)
        print("Seq. In:  {}  \nSeq. Out: {}\n".format(a_string, b_string))
        print("Seq. In:  {}  \nSeq. Out: {}\n".format(a_tuple, b_tuple))

    for i in range(1, 5):
        for j in range(1, 4):
            b_string = remove_n_and_leave_every_mth(a_string, i, j)
            b_tuple = remove_n_and_leave_every_mth(a_tuple, i, j)
            print("remove_n_and_leave_every_mth(seq, n, m),  n = ", i, "  m = ", j)
            print("Seq. In:  {}  \nSeq. Out: {}\n".format(a_string, b_string))
            print("Seq. In:  {}  \nSeq. Out: {}\n".format(a_tuple, b_tuple))

    b_string = reverse(a_string)
    b_tuple = reverse(a_tuple)
    print("reverse(seq):")
    print("Seq. In:  {}  \nSeq. Out: {}\n".format(a_string, b_string))
    print("Seq. In:  {}  \nSeq. Out: {}\n".format(a_tuple, b_tuple))

    b_string = change_slice_order(a_string)
    b_tuple = change_slice_order(a_tuple)
    print("change_slice_order(seq):")
    print("Seq. In:  {}  \nSeq. Out: {}\n".format(a_string, b_string))
    print("Seq. In:  {}  \nSeq. Out: {}\n".format(a_tuple, b_tuple))
