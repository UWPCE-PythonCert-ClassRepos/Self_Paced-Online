#! /usr/bin/env python
def exchange_first_last(s):
    """Swap first and last values."""
    if len(s) < 2:
        return s[:]
    else:
        return s[-1:] + s[1:-1] + s[:1]


def remove_alternate(s):
    """Remove alternate entries."""
    return s[::2]


def center(s):
    """
    Remove first and last four items and return every other item."""
    return s[4:-4:2]


def reverse(s):
    """Return reversed sequence."""
    return s[::-1]


def shell_game(s):
    """Return last third, then first third, then middle third."""
    size = len(s) // 3
    # return s[-size:] + s[:size] + s[size:-size]
    return s[-size:] + s[:-size]


if __name__ == "__main__":

    a_string = 'this is a string'
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == 'ghis is a strint'
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert remove_alternate(a_string) == 'ti sasrn'
    assert remove_alternate(a_tuple) == (2, 13, 5)

    assert center(a_string) == ' sas'
    assert center(a_tuple) == ()

    assert reverse(a_string) == 'gnirts a si siht'
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert shell_game(a_string) == "tringthis is a s"
    assert shell_game(a_tuple) == (5, 32, 2, 54, 13, 12)
