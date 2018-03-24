#!/usr/bin/env python

# Task One


def pad_(num, length=3):
    return ((length - len(str(num)))*'0') + str(num)


def strfor(tup):
    print("file_{}: {:.2f}, {:.2e}, {:.2e}".format(pad_(tup[0]), tup[1], tup[2], tup[3]))


strfor((2, 123.4567, 10000, 12345.67))
# ---------


# Task Two

# ---------


# Task Three


def formatter(dat):
    form_string = "the " + str(len(dat)) + " numbers are: " + "{:d}, "*len(dat)
    return form_string.format(*dat)


print(formatter((2, 3, 5, 7, 9)))


# ---------


# Task Four


def dater(data):
    print("{} {} {} {} {}".format(pad_(data[3], 2), data[4], data[2], pad_(data[0], 2), pad_(data[1], 2)))


dater((4, 30, 2017, 2, 27))


# ---------


# Task Five

# ---------


# Task Six

# ---------