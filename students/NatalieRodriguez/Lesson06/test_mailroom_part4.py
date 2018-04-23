#!/usr/bin/env python3

# Lesson 06: Mailroom: Part 4, With Unit Testing
# Natalie Rodriguez
# April 22, 2018

# !/usr/bin/env python3


import os
import mailroom_part4 as mailroom
import pytest


#tests

def test_create_form_letter_1():
    assert mailroom.create_form_letter('Virginia Ferdinand', 1000) == None

def test_create_form_letter_2():
    assert mailroom.create_form_letter('Luke Rodriguez', -60) == None


if __name__ == "__main__":
    test_create_form_letter_1()
    print("tests pass")


