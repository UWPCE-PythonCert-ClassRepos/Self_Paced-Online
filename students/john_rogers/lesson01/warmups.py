#!/usr/bin/env python3
"""
Warm up exercises
Author: JohnR
"""


def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and b_smile:
        return True
    return False


def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b


def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2


def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    return False


def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10


def near_hundred(n):
    a = range(90, 111)
    b = range(190, 211)
    if n in a or n in b:
        return True
    return False


def pos_neg(a, b, negative):
    if negative:
        return (a < 0 and b < 0)
    else:
        return ((a < 0 and b > 0) or (a > 0 and b < 0))


def not_string(str):
    if len(str) >= 3 and str[:3] == "not":
        return str
    return "not " + str


def string_times(str, n):
    return str * n


def front_times(str, n):
    a = str[:3]
    return a * n


def string_bits(str):
    foo = ""
    for i in range(len(str)):
      if i % 2 == 0:
        foo = foo + str[i]
    return foo


def string_splosion(str):
    foo = ""
    for i in range(len(str)):
        foo = foo + str[:i + 1]
    return foo


def array_count9(nums):
    n = 0
    for c in nums:
        if c == 9:
            n = n + 1
    return n


def array_front9(nums):
    test = nums[:4]
    for i in test:
        if i == 9:
            return True
            break

    return False


def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True

    return False