"""Slicing excercises"""


def exchange_first_last(a_seq):
    """Return a copy of a sequence that has first and last item swapped"""
    return a_seq[-1:] + a_seq[1:len(a_seq) - 1] + a_seq[:1]


def remove_odd(a_seq):
    """Return a copy of a sequence that has first and last item swapped"""
    return a_seq[::2]


def remove_outer_and_skip(a_seq):
    """Return a copy of a string without first and last 4 and skip"""
    if len(a_seq) < 9:
        print("Sequence requires at least 10 paramaters to work.")
    return a_seq[4:len(a_seq) - 4:2]


def reverse_sequence(a_seq):
    """Reverse a sequence using only slicing"""
    return a_seq[::-1]


def something_third(a_seq):
    """Return the middle third, then last third, then the first third"""
    every_third = a_seq[::3]
    number_of_thirds = len(every_third)
    middle_indices_of_third = int(number_of_thirds / 2)
    return every_third[middle_indices_of_third:middle_indices_of_third + 1] + every_third[-1:] + every_third[:1]

a_string = "Slice that bread"
a_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
a_short_tuple = (0, 1, 2, 3, 4, 5)
mixed_tuple = ("zero", 1, "two", 3, "four", 5, "six", 7,
               "eight", 9, "ten", 11, "twelve")
mixed_short_tuple = ("zero", 1, "two", 3, "four", 5, "six")

if __name__ == '__main__':
    print("Test suite exchange first last")
    assert exchange_first_last(a_string) == "dlice that breaS"
    assert exchange_first_last(a_short_tuple) == (5, 1, 2, 3, 4, 0)
    assert exchange_first_last(mixed_short_tuple) == (
        "six", 1, "two", 3, "four", 5, "zero")
    print(" Tests passed.")

    print("Test suite remove odd")
    assert remove_odd(a_string) == "Sieta ra"
    assert remove_odd(a_short_tuple) == (0, 2, 4)
    assert remove_odd(mixed_short_tuple) == ("zero", "two", "four", "six")
    print(" Tests passed.")

    print("Test suite remove outer and skip")
    assert remove_outer_and_skip(a_string) == "eta "
    assert remove_outer_and_skip(a_tuple) == (4, 6, 8, 10)
    assert remove_outer_and_skip(mixed_tuple) == ("four", "six", "eight")
    print(" Tests passed.")

    print("Test suite remove something third")
    assert something_third(a_string) == "tdS"
    assert something_third(a_tuple) == (9, 15, 0)
    assert something_third(mixed_tuple) == ("six", "twelve", "zero")
    print(" Tests passed.")
