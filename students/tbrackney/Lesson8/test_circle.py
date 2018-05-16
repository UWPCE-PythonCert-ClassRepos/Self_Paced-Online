#!/usr/bin/env python3
"""
File Name: circle.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 5/16/2018
Python Version: 3.6.4
"""
import circle
import pytest


def test_radius_constructor():
    c = circle.Circle(4)
    assert c.radius == 4


def test_radius_setter():
    c = circle.Circle(4)
    c.radius = 2
    assert c.radius == 2
    with pytest.raises(ValueError):
        c.radius = -2


def test_diameter():
    c = circle.Circle(7.5)
    assert c.diameter == 15


def test_diameter_setter():
    c = circle.Circle(5)
    c.diameter = 12
    assert c.radius == 6
    with pytest.raises(ValueError):
        c.diameter = -5


def test_area():
    c = circle.Circle(2)
    assert c.area == 12.566370614359172
    with pytest.raises(AttributeError):
        c.area = 12


def test_from_diameter():
    c = circle.Circle.from_diameter(10)
    assert c.radius == 5
    with pytest.raises(ValueError):
        d = circle.Circle.from_diameter(-10)
