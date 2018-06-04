# -------------------------------------#
# Desc: Slicing Lab
# Dev: Will White
# Date: 5/4/2018
# ChangeLog: (When,Who,What)
# -------------------------------------#

def task_1():
    tuple_orig = (2, 123.4567, 10000, 12345.67)
    tuple_formatted = "file_{:03d}, {:3.2f}, {:.2e}, {:.2e}".format(*tuple_orig)
    print(tuple_formatted)


def task_2():
    tuple_orig = (2, 123.4567, 10000, 12345.67)
    tuple_formatted = "file_{:03d}, {:3.2f}, {:.2e}, {:.2e}".format(tuple_orig[0], tuple_orig[1], tuple_orig[2], tuple_orig[3],)
    print(tuple_formatted)


def task_3(new_tuple):
    tuple_len = len(new_tuple)
    dynamic_str = "The list includes {} numbers, they are as follows: ".format(tuple_len) + ", ".join(new_tuple)
    print(dynamic_str)


def task_4():
    tuple_orig = (4, 30, 2017, 2, 27)
    string_new = "{:02d} {} {} {:02d} {}".format(tuple_orig[3], tuple_orig[4], tuple_orig[2], tuple_orig[0], tuple_orig[1])
    print(string_new)


def task_5():
    list_data = ['oranges', 1.3, 'lemons', 1.1]
    f_string = f"The weight of an {list_data[0][:-1]} is {list_data[1]} and the weight of a {list_data[2][:-1]} is {list_data[3]}"
    print(f_string)
    f_string_new = f"The weight of an {list_data[0].upper()[:-1]} is {list_data[1]*1.2} and the weight of a {list_data[2].upper()[:-1]} is {list_data[3]*1.2}"
    print(f_string_new)

def task_6():
    list_data = [['TV', '5', '20.00'],['Couch', '100', '4,000.00'],['Planet', '10,000', '4,000,000.00']]
    for i in list_data:
        print('{:<10}{:>10}{:>20}'.format(*i))

def task_6_bonus():
    tuple_data = tuple(range(10))
    print(('{:5d}'*len(tuple_data)).format(*tuple_data))
