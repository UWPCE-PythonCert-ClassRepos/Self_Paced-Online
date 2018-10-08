#!/usr/bin/env python3

import mailroom4 as mailroom
import sys
import string
import os.path
from collections import defaultdict

def test_donor_list():
    mail_list = mailroom.donor_list()
    assert "Andy" in mail_list
    assert "Bill" in mail_list
    assert "Chuck" in mail_list

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

if __name__ == "__main__":
    test_donor_list()