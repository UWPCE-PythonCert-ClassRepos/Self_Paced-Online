# Lesson_3 Activity 1: Slice lab

# test sequences
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


def exchange_first_last(seq):
    """swap the first and last item in a sequence"""
    return (seq[-1:] + seq[1:-1] + seq[0:1])

assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2),\
 "failed tuple test"
assert exchange_first_last(a_string) == "ghis is a strint",\
 "failed string test"


def skip_every_other(seq):
    """skip every other item in a sequence"""
    return (seq[::2])

assert skip_every_other(a_tuple) == (2, 13, 5),\
 "failed tuple test"
assert skip_every_other(a_string) == "ti sasrn",\
 "failed string test"


def remove_four_skip(seq):
    """remove first and last 4 items and skip every other item in between"""
    return(seq[4:-4:2])

assert remove_four_skip(a_tuple) == (),\
 "failed tuple test"
assert remove_four_skip(a_string) == " sas",\
 "failed string test"


def reverse_sequence(seq):
    """return a reversed sequence"""
    return(seq[::-1])

assert reverse_sequence(a_tuple) == (32, 5, 12, 13, 54, 2),\
 "failed tuple test"
assert reverse_sequence(a_string) == "gnirts a si siht",\
 "failed string test"


def swap_thirds(seq):
    """swap middle third of sequence to front followed by last and then first third"""
    # Used floored division to split into thirds
    thirds = len(seq) // 3
    return(seq[thirds:thirds*2] + seq[thirds*2:] + seq[:thirds])


assert swap_thirds(a_tuple) == (13, 12, 5, 32, 2, 54),\
 "failed tuple test"
assert swap_thirds(a_string) == "is a stringthis ",\
 "failed string test"
assert swap_thirds("this is a random string that is much longer") == \
 "om string that is much longerthis is a rand", "failed other test"
