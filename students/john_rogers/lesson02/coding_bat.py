#!/usr/bin/env python3
"""
codingbat.com exercises, lesson02
Author: JohnR
"""


def hello_name(name):
    return 'Hello ' + name + '!'


def make_abba(a, b):
    return a + b + b + a


def make_tags(tag, word):
    t1 = '<' + tag + '>'
    t2 = '</' + tag + '>'
    return t1 + word + t2


def make_out_word(out, word):
    t1 = out[:2]
    t2 = out[2:]
    return t1 + word + t2


def extra_end(str):
    t = str[-2:]
    return t * 3


def first_two(str):
    if len(str) == 0:
        return ""
    if len(str) <= 2:
        return str
    else:
        return str[:2]


def first_half(str):
    l = len(str) / 2
    return str[:l]


def without_end(str):
    l = str[:-1]
    w = l[1:]
    return w


def combo_string(a, b):
    t1 = len(a)
    t2 = len(b)
    if t1 > t2:
        return b + a + b
    else:
        return a + b + a


def non_start(a, b):
    s1 = a[1:]
    s2 = b[1:]
    return s1 + s2


def left2(str):
    s1 = str[2:]
    s2 = str[:2]
    return s1 + s2


def first_last6(nums):
    f = nums[0]
    l = nums[-1]
    if f == 6 or l == 6:
        return True
    else:
        return False


def same_first_last(nums):
    if len(nums) < 1:
        return False
    f = nums[0]
    l = nums[-1]
    if f == l:
        return True
    else:
        return False


def make_pi():
    l = [3, 1, 4]
    return l


def common_end(a, b):
    af = a[0]
    al = a[-1]
    bf = b[0]
    bl = b[-1]
    if af == bf or al == bl:
        return True
    else:
        return False


def sum3(nums):
    x = 0
    for i in nums:
        x = x + i
    return x









