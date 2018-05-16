#!/usr/bin/env python3
"""
File Name: circle.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 5/16/2018
Python Version: 3.6.4
"""
import math


class Circle():
    def __init__(self, the_radius):
        self._r = the_radius

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError('Radius must be greater than 0')
        self._r = val

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, val):
        if val < 0:
            raise ValueError('Diameter must be greater than 0')
        self._r = val / 2

    @property
    def area(self):
        return math.pi * self._r ** 2

    @classmethod
    def from_diameter(cls, val):
        if val < 0:
            raise ValueError('Diameter must be greater than 0')
        return cls(val / 2)
