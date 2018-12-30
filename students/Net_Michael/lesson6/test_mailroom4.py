#!/usr/bin/env python
# coding: utf-8

import pytest
from mailroom4 import *

import pytest


def test_one():
    with pytest.raises(SystemExit):
        quit_sel()
