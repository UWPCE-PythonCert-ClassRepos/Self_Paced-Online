# ------------------------------------------------- #
# Title: Lesson 3, pt 1/4, Slicing Exercise
# Dev:   Craig Morton
# Date:  8/18/2018
# Change Log: CraigM, 8/18/2018, Slicing Exercise
#  ------------------------------------------------ #

# Sequences
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


def first_last_exchanged(first_seq):
    """First and last items exchanged"""
    second_seq = first_seq[0:0]
    second_seq += first_seq[-1:len(first_seq)]
    second_seq += first_seq[1:-1]
    second_seq += first_seq[0:1]
    return second_seq


assert first_last_exchanged(a_string) == "ghis is a strint"
assert first_last_exchanged(a_tuple) == (32, 54, 13, 12, 5, 2)


def every_other_removed(first_seq):
    """Every other item removed"""
    return first_seq[::2]


assert every_other_removed(a_string) == "ti sasrn"
assert every_other_removed(a_tuple) == (2, 13, 5)


def four_removed(first_seq):
    """First 4 and last 4 items removed, and then every other item in between"""
    return first_seq[4:-4:2]


assert four_removed(a_string) == " sas"
assert four_removed(a_tuple) == ()


def elements_reversed(first_seq):
    """The elements reversed (just with slicing)"""
    return first_seq[::-1]


assert elements_reversed(a_string) == "gnirts a si siht"
assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)


def thirds_switched(first_seq):
    """The middle third, then last third, then the first third in the new order"""
    third = len(first_seq) // 3
    return first_seq[third:] + first_seq[0:third]


assert thirds_switched(a_string) == "is a stringthis "
assert thirds_switched(a_tuple) == (13, 12, 5, 32, 2, 54)

# Presentation
print(first_last_exchanged(a_string))
print(first_last_exchanged(a_tuple))

print(every_other_removed(a_string))
print(every_other_removed(a_tuple))

print(four_removed(a_string))
print(four_removed(a_tuple))

print(elements_reversed(a_string))
print(elements_reversed(a_tuple))

print(thirds_switched(a_string))
print(thirds_switched(a_tuple))
