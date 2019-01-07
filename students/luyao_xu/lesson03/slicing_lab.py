"""Get the basics of sequence slicing down"""


def exchange_first_last(seq):
    """
        Exchange the first item and the last item of a sequence
       :param seq: the sequence
       :return: The first and last item in a sequence exchanged
       """
    if len(seq) <= 1:
        return seq
    return seq[-1:] + seq[1:-1] + seq[:1]


def every_other_removed(seq):
    """
    Remove every other item in a sequence
    :param seq: the sequence
    :return: Every other item removed in a sequence
    """
    return seq[::2]


def every_other_4removed(seq):
    """
    Removed first4 and last 4 items, and then every other item in between of the sequence
    :param seq: The
    :return:
    """
    return seq[4:-4:2]


def reverse_items(seq):
    """
    Elements reverse
    :param seq:  the sequence
    :return:  Reverse elements
    """

    return seq[::-1]


def order_third(seq):
    """
     with the middle third, then last third, then the first third in the new order
    :param seq: The sequence
    :return: new order of sequence: middle third, last third, first third.
    """

    one_third = len(seq) // 3
    return seq[one_third:one_third * 2] + seq[one_third * 2:] + seq[:one_third]


if __name__ == '__main__':
    a_string = "Say hello to the world"
    a_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
    empty = ''
    one_el = 'H'

    assert exchange_first_last(a_string) == "day hello to the worlS"
    assert exchange_first_last(a_tuple) == (8, 2, 3, 4, 5, 6, 7, 1)
    assert exchange_first_last(empty) == ''
    assert exchange_first_last(one_el) == 'H'
    assert every_other_removed(a_string) == "Syhlot h ol"
    assert every_other_removed(a_tuple) == (1, 3, 5, 7)
    assert every_other_removed(empty) == ''
    assert every_other_removed(one_el) == 'H'
    assert reverse_items(a_string) == "dlrow eht ot olleh yaS"
    assert reverse_items(empty) == ''
    assert reverse_items(one_el) == 'H'
    assert reverse_items(a_tuple) == (8, 7, 6, 5, 4, 3, 2, 1)
    assert order_third(a_string) == "lo to the worldSay hel"
    assert order_third(empty) == ''
    assert order_third(one_el) == 'H'
    assert order_third(a_tuple) == (3, 4, 5, 6, 7, 8, 1, 2)
