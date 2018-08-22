# ------------------------------------------------- #
# Title: Lesson 3, pt 3/4, String Formatting Exercise
# Dev:   Craig Morton
# Date:  8/20/2018
# Change Log: CraigM, 8/20/2018, String Formatting Exercise
#  ------------------------------------------------ #

# !/usr/bin/env python3


def first_task():
    """First task - Tuple format string"""
    tuple_one = (2, 123.4567, 10000, 12345.67)

    # create a string formatter to produce:
    # 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    print("file_{:0>3d} :   {:.2f}, {:.2e}, {:.3e}".format(tuple_one[0], tuple_one[1], tuple_one[2], tuple_one[3]))


def second_task():
    """Second task - Using results from first task, use a different type of format string"""
    tuple_two = (2, 123.4567, 10000, 12345.67)
    print(f"file_{tuple_two[0]:0>3d} :   {tuple_two[1]:.2f}, {tuple_two[2]:.2e}, {tuple_two[3]:.3e}")


def third_task(tuple_value):
    """Third task - Dynamically building format strings"""
    tuple_three = "the {} numbers are: ".format(len(tuple_value))

    if len(tuple_value) > 0:
        tuple_three += "{}".format(tuple_value[0])
    for val in tuple_value[1:]:
        tuple_three += ", {}".format(val)
    return tuple_three


def fourth_task(tuple_value_two):
    """Fourth task - Five element tuple and string formatting"""
    print("{n3:0>2d} {n4:0>2d} {n2:0>2d} {n0:0>2d} {n1:0>2d}".format(
        n0=tuple_value_two[0], n1=tuple_value_two[1], n2=tuple_value_two[2],
        n3=tuple_value_two[3], n4=tuple_value_two[4]))


def fifth_task():
    """Fifth Task - Using f-strings"""
    orange = ("orange", 1.3)
    lemon = ("lemon", 1.1)
    print(f"The weight of an {orange[0]} is {orange[1]} and the weight of a {lemon[0]} is {lemon[1]}")
    print(
        f"The weight of an {orange[0].upper()} is {orange[1] * 1.2} "
        f"and the weight of a {lemon[0].upper()} is {lemon[1] * 1.2}")


def sixth_task():
    """Sixth Task - Displaying data in columns and string formatting"""
    lst = list()
    lst.append(("Frodo", 25, 53))
    lst.append(("Bilbo", 71, 142))
    lst.append(("Gandalf", 82, 1089))
    lst.append(("Aragorn", 40, 24593))
    lst.append(("Elrond", 183, 542099))
    lst.append(("Durin", 97, 1000000))

    for d in lst:
        print("{:<20}  {:>3d}  ${:>15.2f}".format(*d))

    extra_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(("{:5d}" * 10).format(*extra_tuple))


first_task()
second_task()
print(third_task(()))
print(third_task((0,)))
print(third_task((1, 2, 3)))
print(third_task((4, 5, 6, 7, 8, 9)))
fourth_task((4, 30, 2017, 2, 27))
fifth_task()
sixth_task()
