#!/usr/bin/env python
# coding: utf-8

import pytest
from mailroom4 import *

import pytest


def test_one():
    with pytest.raises(SystemExit):
        quit_sel()


def test_two():
    test_values = donor_list_dir("donor_list").split("\\")
    assert "donor_list" == test_values[len(test_values)-1]
