#!/usr/bin/env python3

import mailroom as m
import pytest
import sys


#this function can be fleshed out more.
#https://stackoverflow.com/questions/26561822/pytest-capsys-checking-output-and-getting-it-reported
#https://docs.pytest.org/en/latest/reference.html#capsys
#https://docs.pytest.org/en/latest/capture.html
def test_display_list(capsys):
    result = m.display_list()
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)
    assert out.startswith("Manny Machado\nAdam Jones\nChris Davis")

def test_write_letter():
    expected = "Dear Manny,\nThank you for donating $8.00 to the Human Fund. " \
            "Your money will be used appropriately."
    assert m.write_letter("Manny",8) == expected

def test_write_report():
    expected_1 = 'Donor Name                | Total Given | Num Gifts | Average Gift\n' \
                '-'*67 + '\nAdam Jones                 $    1369.80           3  $      456.60'
    expected_3 = 'Adam Jones                 $    1369.80           3  $      456.60'
    #expected = expected_1 + '\n' + expected_2 + '\n' + expected_3
     
    report_input = [[1369.80,'Adam Jones',3,456.60]]
    assert m.write_report(report_input) == expected_1
    #expected.endswith



#m.display_list()


