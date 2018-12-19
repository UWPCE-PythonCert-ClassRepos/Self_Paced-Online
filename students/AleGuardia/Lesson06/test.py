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
    assert return_donors() == ["William Gates, III\n",
                               "Mark Zuckerberg\n","Jeff Bezos\n","Paul Allen\n","Elon Musk\n"]


def test_label():
    assert return_label() == 'Donor Name         |  Total Given | Num Gifts | ' \
                             'Average Gift\n-------------------------------------------------------------'


def test_report():
    assert return_report(donations) == 'Donor Name         |  Total Given | Num Gifts | Average Gift\n' \
                                       '-------------------------------------------------------------\n' \
                                       'William Gates, III $   7335000.00          3  $   2445000.00\n' \
                                       'Mark Zuckerberg    $     20000.00          2  $     10000.00\n' \
                                       'Jeff Bezos         $   3000000.00          1  $   3000000.00\n' \
                                       'Paul Allen         $     26000.00          2  $     13000.00\n' \
                                       'Elon Musk          $     33499.00          2  $     16749.50\n'


def test_print_report():
    assert print_report() == 'Donor Name         |  Total Given | Num Gifts | Average Gift\n' \
                            '-------------------------------------------------------------\n' \
                            'William Gates, III $   7335000.00          3  $   2445000.00\n' \
                            'Mark Zuckerberg    $     20000.00          2  $     10000.00\n' \
                            'Jeff Bezos         $   3000000.00          1  $   3000000.00\n' \
                            'Paul Allen         $     26000.00          2  $     13000.00\n' \
                            'Elon Musk          $     33499.00          2  $     16749.50\n'


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


def make_multi_input(inputs, idx=0):
    """ provides a function to call for every input requested. """

    def next_input(message=""):
        nonlocal idx
        if idx < len(inputs):
            idx = idx + 1
            return inputs[idx - 1]
        else:
            return ""
    return next_input


# Tests logic in prompt
def test_prompt_donors_list(monkeypatch, capsys):
    monkeypatch.setitem(__builtins__,'input',make_multi_input(["list","quit"]))
    prompt_donors()
    out, err = capsys.readouterr()
    assert out == "William Gates, III\n Mark Zuckerberg\n Jeff Bezos\n Paul Allen\n Elon Musk\n Ale\n\n"


# Test adding new donor and donation and report output
def test_add_donation_new_donor(monkeypatch, capsys):
    thank_you_note = "\nDear {}:\n\nWe want to thank you for your generous donation of ${:.2f}.\n\n" \
                     "It will be put to very good use.\n\n" \
                     "\tSincerely,\n\t\tThe Team\n\n"

    expected_output_report = '\nDonor Name         |  Total Given | Num Gifts | Average Gift\n' \
                             '-------------------------------------------------------------\n' \
                             'William Gates, III $   7335000.00          3  $   2445000.00\n' \
                             'Mark Zuckerberg    $     20000.00          2  $     10000.00\n' \
                             'Jeff Bezos         $   3000000.00          1  $   3000000.00\n' \
                             'Paul Allen         $     26000.00          2  $     13000.00\n' \
                             'Elon Musk          $     33499.00          2  $     16749.50\n' \
                             'Ale                $        20.25          1  $        20.25\n' \
                             'Pit                $        50.00          1  $        50.00\n\n'
    expected_output_note = thank_you_note.format('Pit',50)
    monkeypatch.setitem(__builtins__,'input',make_multi_input(['Pit',50]))
    prompt_donors()
    out, err = capsys.readouterr()
    assert out == expected_output_note
    print_report()
    out, err = capsys.readouterr()
    assert out == expected_output_report
