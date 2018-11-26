# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:14:30 2018

@author: Laura.Fiorentino
"""


from sparsearray import SparseArray


def test_length():
    sa = SparseArray([2, 3, 0, 0, 0, 7, 0])
    assert len(sa) == 7
    del sa[1]
    assert len(sa) == 6


def test_del():
    sa = SparseArray([2, 3, 0])
    del sa[0]
    assert sa.array == {0: 3}
    assert len(sa) == 2


def test_get():
    sa = SparseArray([2, 3, 0, 0, 0, 7, 0])
    assert sa[3] == 0
    assert sa[0] == 2


def test_set():
    sa = SparseArray([2, 3, 0, 0, 0, 7, 0])
    sa[0] = 1
    assert sa[0] == 1


def test_append():
    sa = SparseArray([2, 3, 0, 0, 0, 7, 0])
    sa.append(1)
    assert sa[8] == 1
    assert len(sa) == 8
