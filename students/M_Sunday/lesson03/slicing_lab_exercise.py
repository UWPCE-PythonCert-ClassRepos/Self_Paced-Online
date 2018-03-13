# lesson 03 - slicing lab exercise

seq1 = "what a beautiful day"
seq2 = ['red', 'blue', 'orange', 'green', 'yellow', 'cyan', 'magenta', 'violet', 'aqua']
seq3 = (1, 2, 3, 4, 5, 6, 7, 8, 9)


def last_first(seq):
    # This function swaps the first and last items in a sequence
    return seq[-1:] + seq[1:-1] + seq[:1]


def every_other(seq):
    # This function returns every other item in a sequence
    return seq[::2]


def every_other_short(seq):
    # This function returns every other item in a sequence after
    # removing the first four and last four items
    return seq[4:-4:2]


def reversed1(seq):
    # This function reverses the item order in a sequence
    return seq[::-1]


def third_swap(seq):
    # This function orders the items in the sequence with the middle
    # third of the items, the last third, and then the first third
    stop = int(len(seq)/3)
    return seq[stop:-stop] + seq[-stop:] + seq[:stop]


# seq1 = "what a beautiful day"
# seq2 = ['red', 'blue', 'orange', 'green', 'yellow', 'cyan', 'magenta', 'violet', 'aqua']
# seq3 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Testing section
assert last_first(seq1) == "yhat a beautiful daw"
assert last_first(seq2) == ['aqua', 'blue', 'orange', 'green', 'yellow', 'cyan', 'magenta', 'violet', 'red']
assert last_first(seq3) == (9, 2, 3, 4, 5, 6, 7, 8, 1)

assert every_other(seq1) == "wa  euiu a"
assert every_other(seq2) == ['red', 'orange', 'yellow', 'magenta', 'aqua']
assert every_other(seq3) == (1, 3, 5, 7, 9)

assert every_other_short(seq1) == "  euiu"
assert every_other_short(seq2) == ['yellow', ]
assert every_other_short(seq3) == (5,)

assert reversed1(seq1) == "yad lufituaeb a tahw"
assert reversed1(seq2) == ['aqua', 'violet', 'magenta', 'cyan', 'yellow', 'green', 'orange', 'blue', 'red']
assert reversed1(seq3) == (9, 8, 7, 6, 5, 4, 3, 2, 1)

assert third_swap(seq1) == " beautiful daywhat a"
assert third_swap(seq2) == ['green', 'yellow', 'cyan', 'magenta', 'violet', 'aqua', 'red', 'blue', 'orange']
assert third_swap(seq3) == (4, 5, 6, 7, 8, 9, 1, 2, 3)
