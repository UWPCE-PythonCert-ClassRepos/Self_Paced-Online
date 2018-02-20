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
