#!/usr/bin/env python3

import mailroom as m
import pytest

def test_write_letter():
    expected = "Dear Manny,\nThank you for donating $8 to the Human Fund. Your money will be used appropriately."
    assert write_letter("Manny",8) == expected