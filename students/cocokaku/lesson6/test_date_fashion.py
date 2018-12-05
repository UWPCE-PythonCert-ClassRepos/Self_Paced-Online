#!/usr/bin/env python

"""
You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes,
in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded
as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes).
With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).

date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1
"""



# you can change this import to test different versions
from date_fashion import date_fashion
# from cigar_party import cigar_party2 as cigar_party
# from cigar_party import cigar_party3 as cigar_party


def test_1():
    assert date_fashion(5, 10) is 2


def test_2():
    assert date_fashion(5, 2) is 0


def test_3():
    assert date_fashion(5, 5) is 1


def test_4():
    assert date_fashion(3, 3) is 1


def test_5():
    assert date_fashion(10, 2) is 0


def test_6():
    assert date_fashion(2, 9) is 0


def test_7():
    assert date_fashion(9, 9) is 2


def test_8():
    assert date_fashion(10, 5) is 2


def test_9():
    assert date_fashion(2, 2) is 0


def test_10():
    assert date_fashion(3, 7) is 1


def test_11():
    assert date_fashion(2, 7) is 0


def test_12():
    assert date_fashion(6, 2) is 0
