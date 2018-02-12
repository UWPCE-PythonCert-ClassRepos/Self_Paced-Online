def exchange_first_last(seq):
    """Return a sequence with the first and last items switched"""
    return seq[-1:] + seq[1:-1] + seq[:1]

assert exchange_first_last("Happy") == "yappH"
assert exchange_first_last([4, 8, 15, 16, 23, 42]) == [42, 8, 15, 16, 23, 4]
assert exchange_first_last((4, "t", ["UW", "WSU"])) == (["UW", "WSU"], "t", 4)


def rm_alt(seq):
    """Return a sequence with alternate items removed"""
    return seq[::2]

assert rm_alt("Happy") == "Hpy"
assert rm_alt([4, 8, 15, 16, 23, 42]) == [4, 15, 23]
assert rm_alt((4, "t", ["UW", "WSU"])) == (4, ["UW", "WSU"])


def alt_mid(seq):
    """Return alternate items from a seq with the first/last 4 items removed"""
    return seq[4:-4:2]

assert alt_mid("xxxxabababxxx") == "aaa"
assert alt_mid([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) == [3, 8]


def reversed(seq):
    """Return a sequence in reverse order"""
    return seq[::-1]

assert reversed("Happy") == "yppaH"
assert reversed([4, 8, 15, 16, 23, 42]) == [42, 23, 16, 15, 8, 4]


def thirds(seq):
    """Return a sequence in this order: mid Third, last third, first third"""
    '''I want to round the slice points so the remainders don't
    automatically just go to the last third'''
    first = round(len(seq)/3)
    second = round(2*len(seq)/3)
    return seq[first:second] + seq[second:] + seq[:first]

assert thirds("Happy!") == "ppy!Ha"
assert thirds([4, 8, 15, 16, 23, 42]) == [15, 16, 23, 42, 4, 8]
assert thirds("12345678") == "45678123"
