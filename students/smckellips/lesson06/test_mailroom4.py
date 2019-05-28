#! /usr/bin/env python
import os
import mailroom4 as mailroom

mailroom.donor_db = mailroom.get_donor_db()

def test_donor_db():
    assert len(mailroom.donor_db.keys()) == 4


def test_get_donor():
    donor = mailroom.get_donor('PAUL ALLEN')
    assert donor[0] == 'Paul Allen'


def test_get_donor_missing():
    donor = mailroom.get_donor('Abe Froman')
    assert donor == None


def test_add_donor():
    donor = mailroom.add_donor('Abe Froman')
    donor[1].append(1000)
    assert donor[0] == 'Abe Froman'
    assert mailroom.get_donor(donor[0]) == donor


def test_add_donor_existing():
    donor = mailroom.add_donor('Jeff Bezos')
    assert donor == None


def test_list_donors():
    donor_list = mailroom.list_donors()
    assert 'Jeff Bezos' in donor_list


def test_write_report():
    report = mailroom.write_report()
    assert report.startswith("Donor Name                | Total Given | Num Gifts | Average Gift")
    assert report.__contains__("Paul Allen")


def test_write_letter():
    letter = mailroom.write_letter('Paul Allen')
    assert letter == "Thank you, Paul Allen, for your kind donation of $1.32"


def test_send_letters():
    mailroom.send_letters()
    assert os.path.isfile('Paul_Allen.txt')
    with open('Paul_Allen.txt', 'r') as f:
        letter = f.read()
        assert letter == "Thank you, Paul Allen, for your kind donation of $1.32"

if __name__ == "__main__":
    test_donor_db()
    test_get_donor()
    test_get_donor_missing()
    test_add_donor()
    test_add_donor_existing()
    test_list_donors()
    test_write_report()
    print("All tests passed.")