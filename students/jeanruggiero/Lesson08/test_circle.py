#!/usr/bin/env python3

import pytest
import math

import circle

c1 = circle.Circle(5)

def test_init():
    assert c1.radius == 5

def test_properties():
    assert c1.area == 25*math.pi
    assert c1.diameter == 10
