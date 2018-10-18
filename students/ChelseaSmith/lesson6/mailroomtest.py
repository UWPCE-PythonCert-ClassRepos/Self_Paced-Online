#!/usr/bin/env python3

import mailroompt4
import os


def test_report():
    assert mailroompt4.report({"Alex Smith": [200, 200, 200]}) == ("Donor name" + " " * 17 + " | Total Given | Num Gifts | Average Gift\n" + "Alex Smith        $      600.00         3   $       200.00")


def test_checknew():
    assert mailroompt4.checknew({"Chelsea": [100]}, "Chelsea") == True


def test2_checknew():
    assert mailroompt4.checknew({"Chelsea": [100]}, "Chelsea") == False


def test_writenote():
    assert mailroompt4.writenote("Chelsea", [100]) == "Dear Chelsea,\nThank you for your generous donation of $100.00.\nSincerely,\n Generic Charities"


def test_saveletter():
    mailroompt4.saveletter("Bob.txt", "test")
    assert os.path.isfile("Bob.txt")


def test_letters():
    mailroompt4.letters({"Chelsea": [100]})
    assert os.path.isfile("Chelsea.txt")