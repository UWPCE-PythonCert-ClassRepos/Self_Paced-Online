# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 13:35:41 2018

@author: Laura.Fiorentino
"""
from caught_speeding import caught_speeding


def test_1():
    assert caught_speeding(60, False) == 0


def test_2():
    assert caught_speeding(65, False) == 1


def test_3():
    assert caught_speeding(65, True) == 0


def test_4():
    assert caught_speeding(80, False) == 1


def test_5():
    assert caught_speeding(85, False) == 2


def test_6():
    assert caught_speeding(85, True) == 1
