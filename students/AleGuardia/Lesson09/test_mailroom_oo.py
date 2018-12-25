
from mailroom_oo import *

# Create Donor Collection for testing
donors = Donors()
d1 = Donor("William Gates, III")
d2 = Donor("Mark Zuckerberg")
d3 = Donor("Jeff Bezos")
d4 = Donor("Paul Allen")
d5 = Donor("Elon Musk")
donor_list = [d1, d2, d3, d4, d5]
for donor in donor_list:
    donors.add_donor(donor)
d1.add_donation(1000000)
d1.add_donation(585000)
d1.add_donation(5750000)
d2.add_donation(15000)
d2.add_donation(5000)
d3.add_donation(3000000)
d4.add_donation(25000)
d4.add_donation(1000)
d5.add_donation(30000)
d5.add_donation(3499)


def test_donor_name():
    d = Donor("Alejandro Guardia")
    assert d.name == "Alejandro Guardia"


def test_donations_init():
    d = Donor("Alejandro Guardia")
    assert d.donations == []


def test_add_donation():
    d = Donor("Alejandro Guardia")
    d.add_donation(25)
    assert d.donations == [25]
    d.add_donation(50)
    assert d.donations == [25,50]


def test_total_donations():
    d = Donor("Alejandro Guardia")
    d.add_donation(25)
    d.add_donation(50)
    d_two = Donor("Inge")
    assert d.total_donations() == 75
    assert d_two.total_donations() == 0


def test_average_donation():
    d = Donor("Alejandro Guardia")
    d.add_donation(25)
    d.add_donation(50)
    assert d.average_donation() == 37.5


def test_donors_init():
    donors_test = Donors()
    return donors_test.donors == []


def test_add_donor():
    donors_test = Donors()
    d = Donor("Alejandro Guardia")
    donors_test.add_donor(d)
    assert donors_test.donors[0].name == "Alejandro Guardia"


def test_return_donors():
    donors_test = Donors()
    d = Donor("Alejandro Guardia")
    d_two = Donor("Elon Musk")
    d_three = Donor("Peter Pan")
    donor_list_test = [d,d_two,d_three]
    for donor_test in donor_list_test:
        donors_test.add_donor(donor_test)
    assert donors_test.return_donors() == ["Alejandro Guardia", "Elon Musk", "Peter Pan"]


def test_donor_existence():
    for donor in donor_list:
        donors.add_donor(donor)
    assert donors.donor_existence("Elon Musk")
    assert donors.donor_existence("Roger Rabitt") == False


def test_donor_summary():
    result = donors.donor_summary()
    assert result[0]['name'] == 'William Gates, III'
    assert result[0]['total'] == 7335000
    assert result[0]['number'] == 3
    assert result[0]['average'] == 2445000
    assert result[1]['name'] == 'Mark Zuckerberg'
    assert result[1]['total'] == 20000
    assert result[1]['number'] == 2
    assert result[1]['average'] == 10000
    assert result[2]['name'] == 'Jeff Bezos'
    assert result[2]['total'] == 3000000
    assert result[2]['number'] == 1
    assert result[2]['average'] == 3000000


def test_report():
    donors = Donors()
    d1 = Donor("William Gates, III")
    d2 = Donor("Mark Zuckerberg")
    d3 = Donor("Jeff Bezos")
    d4 = Donor("Paul Allen")
    d5 = Donor("Elon Musk")
    donor_list = [d1, d2, d3, d4, d5]
    for donor in donor_list:
        donors.add_donor(donor)
    d1.add_donation(1000000)
    d1.add_donation(585000)
    d1.add_donation(5750000)
    d2.add_donation(15000)
    d2.add_donation(5000)
    d3.add_donation(3000000)
    d4.add_donation(25000)
    d4.add_donation(1000)
    d5.add_donation(30000)
    d5.add_donation(3499)
    assert donors.return_report() == 'Donor Name         |  Total Given | Num Gifts | Average Gift\n' \
                                       '-------------------------------------------------------------\n' \
                                       'William Gates, III $   7335000.00          3  $   2445000.00\n' \
                                       'Mark Zuckerberg    $     20000.00          2  $     10000.00\n' \
                                       'Jeff Bezos         $   3000000.00          1  $   3000000.00\n' \
                                       'Paul Allen         $     26000.00          2  $     13000.00\n' \
                                       'Elon Musk          $     33499.00          2  $     16749.50\n'


def test_return_donor():
    assert donors.return_donor("Elon Musk").number_donations() == 2


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


def test_prompt_donors_quit(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 'quit')
    assert prompt_donors() is None


def test_prompt_donors_list(monkeypatch, capsys):
    monkeypatch.setitem(__builtins__,'input',make_multi_input(["list","quit"]))
    prompt_donors()
    out, err = capsys.readouterr()
    print(out)
    assert out == '\nWilliam Gates, III\nMark Zuckerberg\nJeff Bezos\nPaul Allen\nElon Musk\n\n'






