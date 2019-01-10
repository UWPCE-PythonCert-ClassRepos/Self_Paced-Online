#!/usr/bin/env python

"""This module contains test functions for the mailroom4 assignment."""

import pytest
import datetime
import mailroom4
from mailroom4 import donors

def test1():
    """Check that the MainMenu exception is raised correctly."""
    with pytest.raises(mailroom4.MainMenu):
        mailroom4.donor_name('return')

def test2():
    """Check that the MainMenu exception is raised correctly."""
    with pytest.raises(mailroom4.MainMenu):
        mailroom4.donor_name('RETURN')

def test3():
    """Check that an input of list returns None
    (implying print_names was called)"""
    assert mailroom4.donor_name('list') is None

def test4():
    """Check that an input of list returns None
    (implying print_names was called)
    """
    assert mailroom4.donor_name('LIST') is None

def test5():
    """Verify input of any other string returns True"""
    assert mailroom4.donor_name('somename') is True

def test6():
    """Verify entering a non-numerical value returns None"""
    assert mailroom4.donor_amount('string','han solo') is None

def test7():
    """Check that the MainMenu exception is raised correctly."""
    with pytest.raises(mailroom4.MainMenu):
        mailroom4.donor_amount('return','somename')

def test8():
    """Verify donor_amount returns True with appropriate input."""
    assert mailroom4.donor_amount('45','han solo') == True

def test9():
    """Verify donor_amount raises a KeyError for a name not in donors.
    This exception is intentionally not caught as it could only result
    from an error in the code.
    """
    with pytest.raises(KeyError):
        mailroom4.donor_amount('45','random_name')

def test10():
    """Verify compose_email works properly with correct input."""
    # Strip leading whitespace since pytest seems to add it for some reason.
    assert mailroom4.compose_email('han solo').lstrip() == """Dear Han Solo,\n
        Thank you so much for your generous donation of $45.00.\n
        We really appreciate your donations totalling $4004.54. You are
        $999995995.46 away from a gift of Spaceballs: The Flamethrower!\n
        Sincerely, The Wookie Foundation
        """
def test11():
    """Verify compose_email raises a KeyError for a name not in donors.
    This exception is intentionally not caught as it could only result
    from an error in the code.
    """
    with pytest.raises(KeyError):
        mailroom4.compose_email('random_name')

def test12():
    """Integration test of add_donation with correct inputs."""
    assert mailroom4.add_donation('han solo','45') == True

def test13():
    """Integration test of add_donation with name not in donors."""
    assert mailroom4.add_donation('new_name','45') == True

def test14():
    """Check that size_report generates the correct size for a test dict."""
    some_dict = {
        '12345': {'name': '12345', 'donations': [1000.0111, 457, 34.2]},
        '1234567890123456789': {'name': '1234567890123456789',
            'donations': [5286286.3, 567, 23.5678]}
        }
    assert mailroom4.size_report(some_dict) == [19, 11, 9, 12]

def test15():
    """Verify filenames are built correctly."""
    info = {'name': 'some name', 'donations': [1000.0111, 457, 34.2]}
    d = datetime.date.today()
    assert mailroom4.build_filename(info) == 'some_name_' + str(d.month) + \
        '_' + str(d.day) + '_' + str(d.year) +'.txt'
