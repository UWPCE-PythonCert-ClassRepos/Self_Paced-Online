#!/usr/bin/python

# Task 1
nums = (2, 123.4567, 10000, 12345.67)

# print("{0}{1:03d}, {2:.2f}, {3:.02e}, {4:.02e}".format('file_', *nums).replace(',', ':', 1))

# Task 2

# print("{file}{file_num:03d}, {num2:.2f}, {num3:.02e}, {num4:.02e}".format(file = 'file_', file_num = 2, num2 = 123.4567, num3 = 10000, num4 = 12345.67).replace(',', ':', 1))

# Task 3

# in_tuple = (2,3,5,7,9)
# in_tuple = (2, 3, 5)


def formatter(in_tuple):
    length = len(in_tuple)
    tup = "{}" + (", {}" * (length - 1))
    counter = "the {} numbers are: {}".format(length, tup)
    return (counter.format(*in_tuple))

# formatter(in_tuple)

# Task 4


tup = (4, 30, 2017, 2, 27)


def modify_tuple(tup):
    local_list = []
    local_list = tup[:]
    string = "{0:>02.1} {1} {2} {3:>02.1} {4}".format(str(local_list[0] / 2), str(local_list[1] - 3), local_list[2], str(local_list[3] * 2), str(local_list[4] + 3))
    print(string)

# modify_tuple(tup)

# Task 5


fruits_and_weight = ['orange', 1.3, 'lemon', 1.1]


def modify_fruit_and_weight(fruits_and_weight):
    orange = fruits_and_weight[0]
    orange_weight = fruits_and_weight[1]
    lemon = fruits_and_weight[2]
    lemon_weight = fruits_and_weight[3]
    print(f"The weight of an {orange} is {orange_weight} and the weight of a {lemon} is {lemon_weight}")
    print(f"The weight of an {orange.upper()} is {orange_weight * 1.2} and the weight of a {lemon.upper()} is {lemon_weight * 1.2}")

# modify_fruit_and_weight(fruits_and_weight)

# Task 6


rows = [['Chandon', 3, '$55'], ['Merlot', 8, '$66'], ['Cheval Blanc', 852, '$135125']]


def wine_age_cost(rows):
    i = 0
    while i < len(rows):
        print('A bottle of {:<13} is {:3} months old and costs {:7} generally.'.format(*rows[i]))
        i += 1


wine_age_cost(rows)
