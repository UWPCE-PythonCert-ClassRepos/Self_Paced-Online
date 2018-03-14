a_string = "this is a string"
a_tuple = ("sardine", 55, "mango", 22, "cashew", 81, "garbanzo", 16, "pesto")
a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


def exchange_first_last(s):
    # exchange the first and last items in a sequence
    return s[-1:] + s[1:-1] + s[:1]


def remove_every_other(s):
    # remove every other item in a sequence
    return s[::2]


def remove_first_last_4_every_other(s):
    # remove the first and last 4 items and every other item in a sequence
    return s[4:-4:2]


def reverse(s):
    # reverse the order of a sequence
    return s[::-1]


def thirds(s):
    # middle third first, last third second, first third last
    third = len(s[::3])
    print(third)
    return s[third:third*2] + s[third*2:] + s[:third]


# assertion testing

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == ("pesto", 55, "mango", 22, "cashew", 81, "garbanzo", 16, "sardine")
assert exchange_first_last(a_list) == [14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0]

assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == ("sardine", "mango", "cashew", "garbanzo", "pesto")
assert remove_every_other(a_list) == [0, 2, 4, 6, 8, 10, 12, 14]

assert remove_first_last_4_every_other(a_string) == " sas"
assert remove_first_last_4_every_other(a_tuple) == ("cashew",)
# I'm actually not sure why there needs to be a left over comma here
# it seems like it should just be a tuple with a single item "cashew"
assert remove_first_last_4_every_other(a_list) == [4, 6, 8, 10]

assert reverse(a_string) == 'gnirts a si siht'
assert reverse(a_tuple) == ('pesto', 16, 'garbanzo', 81, 'cashew', 22, 'mango', 55, 'sardine')
assert reverse(a_list) == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

assert thirds(a_string) == 's a stringthis i'
assert thirds(a_tuple) == (22, 'cashew', 81, 'garbanzo', 16, 'pesto', 'sardine', 55, 'mango')
assert thirds(a_list) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4]
