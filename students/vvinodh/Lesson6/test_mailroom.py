from mailroom import report, letters, donor_list
import os

#test mailroom functions using pytest


def test_report():
    actual = report()
    expected = (
        "-------------------- REPORT --------------------\n"
        "Donor Name         | Total Given    | Num Gifts| Average Gift\n"
        "---------------------------------------------------------------\n"
        "William Gates, III   $    980678.73           3  $ 326892.91\n"
        "Mark Zuckerberg      $     21864.47           3  $   7288.16\n"
        "Jeff Bezos           $      1755.66           3  $    585.22\n"
        "Paul Allen           $       947.56           3  $    315.85\n")


    assert expected == actual


def test_letters():
    assert os.path.isfile('William Gates, III_2018-06-25.txt')
    assert os.path.isfile('Paul Allen_2018-06-25.txt')
    assert os.path.isfile('Mark Zuckerberg_2018-06-25.txt')
    assert os.path.isfile('Jeff Bezos_2018-06-25.txt')


def test_list():
    actual = donor_list()
    expected = ['William Gates, III',
                'Mark Zuckerberg',
                'Jeff Bezos',
                'Paul Allen']

    assert expected == actual
