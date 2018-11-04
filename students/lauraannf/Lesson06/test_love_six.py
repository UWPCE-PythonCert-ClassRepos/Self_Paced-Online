# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 14:24:55 2018

@author: Laura.Fiorentino
"""

from love_six import love_six


def test_1():
    assert love_six(6, 6) is True


def test_2():
    assert love_six(1, 6) is True


def test_3():
    assert love_six(6, 1) is True


def test_4():
    assert love_six(3, 3) is True


def test_5():
    assert love_six(11, 5) is True


def test_6():
    assert love_six(4, 10) is True


def test_7():
    assert love_six(2, 5) is False
