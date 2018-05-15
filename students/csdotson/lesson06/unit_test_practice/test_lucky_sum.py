"""
Given 3 int values, a b c, return their sum.

However, if one of the values is 13 then it does not count towards the sum and values to its right do not count.

So for example, if b is 13, then both b and c do not count
"""

from lucky_sum import lucky_sum

def test_1():
    assert lucky_sum(1, 2, 3) is 6

def test_2():
    assert lucky_sum(1, 2, 13) is 3

def test_3():
    assert lucky_sum(1, 13, 3) is 1

def test_4():
    assert lucky_sum(1, 13, 13) is 1

def test_5():
    assert lucky_sum(6, 5, 2) is 13

def test_6():
    assert lucky_sum(13, 2, 3) is 0

def test_7():
    assert lucky_sum(13, 2, 13) is 0

def test_8():
    assert lucky_sum(13, 13, 2) is 0

def test_9():
    assert lucky_sum(9, 4, 13) is 13

def test_10():
    assert lucky_sum(8, 13, 2) is 8

def test_11():
    assert lucky_sum(7, 2, 1) is 10

def test_12():
    assert lucky_sum(3, 3, 13) is 6
