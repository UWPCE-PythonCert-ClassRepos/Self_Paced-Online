# tests for Mailroom_four.py by Alejandro Guardia

from mailroom_four import return_average
from mailroom_four import return_donors
from mailroom_four import return_label
from mailroom_four import return_report
from mailroom_four import add_donor
from mailroom_four import add_donation
from mailroom_four import prompt_donors
from mailroom_four import print_report

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


def test_print_report():
    assert print_report()== 'Donor Name         |  Total Given | Num Gifts | Average Gift\n-------------------------------------------------------------\nWilliam Gates, III $   7335000.00          3  $   2445000.00\nMark Zuckerberg    $     20000.00          2  $     10000.00\nJeff Bezos         $   3000000.00          1  $   3000000.00\nPaul Allen         $     26000.00          2  $     13000.00\nElon Musk          $     33499.00          2  $     16749.50\n'


def test_donor():
    assert add_donor('Ale') == {'William Gates, III': [1000000, 585000, 5750000],
                                'Mark Zuckerberg': [15000, 5000],
                                'Jeff Bezos': [3000000],
                                'Paul Allen': [25000, 1000],
                                'Elon Musk': [30000, 3499],
                                'Ale': []}


def test_donation(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "20.25")
    assert add_donation('Ale') == 20.25


def test_prompt_donors_quit(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 'quit')
    assert prompt_donors() is None


def makeMultiInput(inputs, idx=0):
    """ provides a function to call for every input requested. """

    def next_input(message=""):
        # nonlocal only in python3 similar to global but
        # for non local non global variables
        nonlocal idx
        if idx < len(inputs):
            idx = idx + 1
            return inputs[idx - 1]
        else:
            return ""
    return next_input


def test_prompt_donors_list(monkeypatch, capsys):
    monkeypatch.setitem(__builtins__,'input',makeMultiInput(["list","quit"]))
    prompt_donors()
    out, err = capsys.readouterr()
    assert out == "William Gates, III\n Mark Zuckerberg\n Jeff Bezos\n Paul Allen\n Elon Musk\n Ale\n\n"



