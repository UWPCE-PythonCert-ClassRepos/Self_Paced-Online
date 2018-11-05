#!/usr/bin/env python

"""
Test script for args and kwargs lab
"""


# testing lab
from args_kwargs_lab import args_kwargs


def test_1():
    assert args_kwargs(
        fcolor="blue",
        bcolor="green",
        lcolor="white",
        vcolor="red") == ('blue', 'green', 'white', 'red')


def test_2():
    assert args_kwargs(
        "blue",
        lcolor="green",
        bcolor="white",
        vcolor="red") == ('blue', 'white', 'green', 'red')


def test_3():
    assert args_kwargs(
        "blue",
        "green",
        "white",
        "red") == ('blue', 'green', 'white', 'red')


def test_4():
    assert args_kwargs(
        "blue",
        "white",
        "red") == ('blue', 'white', 'red', 'blue')


def test_5():
    regular = ("red", "blue")
    links = {"lcolor": "chartreuse", "vcolor": "pink"}
    assert args_kwargs(
        *regular,
        **links) == ('red', 'blue', 'chartreuse', 'pink')
