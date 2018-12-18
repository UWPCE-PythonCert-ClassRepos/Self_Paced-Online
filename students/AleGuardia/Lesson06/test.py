# tests for Mailroom_four.py by Alejandro Guardia

from mailroom_four import return_average
from mailroom_four import return_donors
from mailroom_four import return_label
from mailroom_four import return_report
from mailroom_four import add_donor


donations = {'William Gates, III': [1000000, 585000, 5750000],
             'Mark Zuckerberg': [15000, 5000],
             'Jeff Bezos': [3000000],
             'Paul Allen': [25000,1000],
             'Elon Musk': [30000,3499]}


def test_average():
    assert return_average([5,5,5,10]) == 6.25


def test_donors():
    assert return_donors() == ["William Gates, III\n","Mark Zuckerberg\n","Jeff Bezos\n","Paul Allen\n","Elon Musk\n"]


def test_label():
    assert return_label() == 'Donor Name         |  Total Given | Num Gifts | Average Gift\n-------------------------------------------------------------'


def test_report():
    assert return_report(donations) == 'Donor Name         |  Total Given | Num Gifts | Average Gift\n-------------------------------------------------------------\nWilliam Gates, III $   7335000.00          3  $   2445000.00\nMark Zuckerberg    $     20000.00          2  $     10000.00\nJeff Bezos         $   3000000.00          1  $   3000000.00\nPaul Allen         $     26000.00          2  $     13000.00\nElon Musk          $     33499.00          2  $     16749.50\n'


def test_donor():
    assert add_donor('Ale') == {'William Gates, III': [1000000, 585000, 5750000],
                                'Mark Zuckerberg': [15000, 5000],
                                'Jeff Bezos': [3000000],
                                'Paul Allen': [25000, 1000],
                                'Elon Musk': [30000, 3499],
                                'Ale': []}






