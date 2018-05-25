#!/usr/bin/env python3

# Lesson_6 Activity 1 Test Mailroom Part 4

from Mailroom_Pt4 import *
import os.path


def test_add_donation():
    add_donation('James Franconstein', 3009375072340)
    assert 'James Franconstein' in donor_chart.keys()
    assert 3009375072340 in donor_chart['James Franconstein']


def test_create_report():
    report_test = create_report()
    for item in donor_chart.items():
        assert item[0] in report_test
        assert f"{sum(item[1]):.2f}" in report_test


def test_send_letters_1():
    send_letters("somewhere_over_the_rainbow")
    for item in donor_chart.items():
        assert os.path.isfile((item[0] + ".txt"))


def test_send_letters_2():
    test_dump = "C:\\Users\\chris.kenyon\\Documents\\"
    "Kenyon\\UWPython\\Testing_File_dump"
    send_letters(test_dump)
    for item in donor_chart.items():
        assert os.path.isfile((os.path.join(test_dump, item[0] + ".txt")))


def test_get_key():
    for donor in donor_chart.items():
        sumlist = get_key(donor)
        assert sumlist == sum(donor[1])
