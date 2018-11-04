import pytest
import os
import mailroom4
from mailroom4 import *


def test_letter():
    assert letter("Bill Gates", 78000) == "Dear Bill Gates, thank you for your generous donation in the amount of $78000!"


def test_show_list(capsys):
    show_list()
    captured = capsys.readouterr()
    assert captured.out == ("Bill Gates\n"
                            "Jeff Bezos\n"
                            "Hannah Smith\n"
                            "John Clark\n"
                            "Andrew Jones\n")



def test_stat_donors(capsys):
    stat_donors()
    captured = capsys.readouterr()
    assert captured.out == ("Hannah Smith         $1,000,000.00     2       $  500,000.00\n"
                            "Bill Gates           $  650,000.00     2       $  325,000.00\n"
                            "Andrew Jones         $  171,000.00     3       $   57,000.00\n"
                            "Jeff Bezos           $  107,400.00     3       $   35,800.00\n"
                            "John Clark           $   70,000.00     2       $   35,000.00\n")


def test_create_report(capsys):
    create_report()
    captured = capsys.readouterr()
    assert captured.out == ("Donor Name           Total Given   Num Gifts   Average Gift\n"
                            "--------------------------------------------------------------\n"
                            "Hannah Smith         $1,000,000.00     2       $  500,000.00\n"
                            "Bill Gates           $  650,000.00     2       $  325,000.00\n"
                            "Andrew Jones         $  171,000.00     3       $   57,000.00\n"
                            "Jeff Bezos           $  107,400.00     3       $   35,800.00\n"
                            "John Clark           $   70,000.00     2       $   35,000.00\n") 



