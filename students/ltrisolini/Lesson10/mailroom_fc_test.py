#!/usr/bin/env python3
import mailroom_fc_2 as mr
import sys
import string
import os.path
from collections import defaultdict

Andy = mr.Donor('Andy', [10.00])
Bill = mr.Donor('Bill', [15.00, 25.00])
Chuck = mr.Donor('Chuck', [20.00, 30.00, 40.00])
mailroom = mr.Roster([Andy, Bill, Chuck])

'''def test_donor_list():
    mail_list = mailroom.donor_report()
    assert "Andy" in mail_list
    assert "Bill" in mail_list
    assert "Chuck" in mail_list'''

def test_donor_report():
    report = mailroom.donor_report()
    assert 'Andy' in report
    assert 'Bill' in report
    assert 'Chuck' in report

def test_batch_file():
    mailroom.batch_file()
    assert os.path.isfile("Andy.txt")
    assert os.path.isfile("Bill.txt")
    assert os.path.isfile("Chuck.txt")

def test_projection():
    assert mailroom.donation_projection(3, 1, 50) == 420.0
    assert mailroom.donation_projection(4, 20, 30) == 300.0
    assert mailroom.donation_projection(5, 0, 100) == 700.0

def test_map_filter():
    assert 30.0 in mailroom.map_filter(3, [10.0], 1, 50)
    assert 100.0 in mailroom.map_filter(4, [25.0], 10, 30)
    assert 60.0 in mailroom.map_filter(2, [30.0], 25, 35)

if __name__ == "__main__":

    test_projection()
    test_map_filter()
    test_donor_report()
    test_batch_file()
