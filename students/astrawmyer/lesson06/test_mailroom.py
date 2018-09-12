#!/usr/bin/env python3

import mailroom as m
import pytest
import sys



def test_display_list(capsys):
    result = m.display_list()
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)
    assert out.startswith("Man")

def test_write_letter():
    expected = "Dear Manny,\nThank you for donating $8.00 to the Human Fund. " \
            "Your money will be used appropriately."
    assert m.write_letter("Manny",8) == expected

#m.display_list()