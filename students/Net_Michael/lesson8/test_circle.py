#!/usr/bin/env python
# coding: utf-8

import math
import pytest
import circle as c
   #
def test_inst_attr():
   out = c.Circle(2)
   out.radius = 2
   assert out.radius == 2
   assert out.diameter == 4
   #
def test_propset():
   out = c.Circle(2)
   out.diameter = 6
   assert out.diameter == 6
   assert out.radius == 3
   #
def test_sign():
   with pytest.raises(ValueError):
      raise ValueError("Radius can't be less than zero")
      #
def test_area():
   out = c.Circle(4)
   assert out.area == math.pi * 4**2
     #
def test_repr_and_str():
   out = c.Circle(3)
   assert str(out) =='Circle with radius: 3.0000'
   assert repr(out) =='Circle(3)'
   #
def test_add():
   out1 = c.Circle(1)
   out2 = c.Circle(2)
   out3 = out1 + out2
   assert repr(out1 + out2) == repr(out3)
   assert out3.radius == 3
   #
   #
def test_multiply():
   out1 = c.Circle(4)
   out2 = out1 * 3
   out3 = 3 * out1
   assert out2 == out3 == 12
   #
   #
def testsort_key():
   out = [c.Circle(6), c.Circle(7), c.Circle(8), c.Circle(4), c.Circle(0), c.Circle(2), c.Circle(3), c.Circle(5), c.Circle(9), c.Circle(1)]
   sort_out = sorted(out, key = c.Circle.sort_key)
   assert sort_out[0] == c.Circle(0)
   assert sort_out[-1] == c.Circle(9)
