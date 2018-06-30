#!/usr/bin/env python3
# Ian Letourneau
# 6/18/2018
# Test script for mailroomOO.py

import mailroomFP as m

# Test Map Functionality within challenge function


def test_map_functionality():
    new_db = m.challenge(5)
    assert new_db['LeBron James'] == (
        [435.0, 17.5, 225.0, 3745.05])

# Test minimum and maximum functionality within
# challenge function


def test_setting_bounds():
    new_db = m.challenge(5, mini=7, maxi=1000)
    assert new_db['LeBron James'] == (
        [435.0, 225.0, 3745.05])

    min_db = m.challenge(5, mini=7)
    assert min_db['LeBron James'] == (
        [435.0, 225.0, 3745.05])

    max_db = m.challenge(5, maxi=1000)
    assert max_db['LeBron James'] == (
        [435.0, 17.5, 225.0, 3745.05])

# Test projection functionality in challenge function


def test_projection():
    prop1_db = m.challenge(2, maxi=100, total=True)
    assert prop1_db['LeBron James'] == (271.0)

    prop2_db = m.challenge(3, mini=50, total=True)
    assert prop2_db['LeBron James'] == (2508.0299999999997)
