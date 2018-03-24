#!/usr/bin/env python

# Task One


def pad_(num, length=3):
    return ((length - len(str(num)))*'0') + str(num)


def strfor(tup):
    print("file_{}: {:.2f}, {:.2e}, {:.2e}".format(pad_(tup[0]), tup[1], tup[2], tup[3]))


strfor((2, 123.4567, 10000, 12345.67))
# ---------


# Task Two


def strforf(tup):
    print(f"file_{pad_(tup[0])}:" + " {:.2f}, {:.2e}, {:.2e}".format(tup[1], tup[2], tup[3]))


strforf((2, 123.4567, 10000, 12345.67))
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


def f_string(li, text_type=0, ratio=0):
    if text_type == 1:
        li[0] = li[0].upper()
        li[2] = li[2].upper()
    print(f"The weight of an {li[0][:-1]} is {li[1]*(1+ratio/100)} and the weight of a "
          f"{li[2][:-1]} is {li[3]*(1+ratio/100)}")


f_string(["oranges", 1.3, "lemons", 1.1])
f_string(["oranges", 1.3, "lemons", 1.1], 1, 20)
# ---------


# Task Six


dataset = [["Joe", 25, 45098],
           ["Sarah", 39, 109843],
           ["Marge", 71, 156],
           ["Roger", 15, 1023.98],
           ["Cindy", 65, 12340.5],
           ["Stephanie", 34, 123.34],
           ["John", 86, 1236.43]]

for row in dataset:
    print("{:<10} {:<4} ${:<7}".format(*row))

tu = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
str_for = "{:<5}"*len(tu)
print(str_for.format(*tu))
# ---------
