# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:09:24 2018

@author: Laura.Fiorentino
"""


from mailroom_4 import create_report, add_donation, write_email, create_folder, donor_list
import os, datetime

def test_create_report(capsys):
    create_report()
    out, err = capsys.readouterr()
    test_string = ('-------List of Donors-------\n'
'Donor Name          Total Donated       # of donations      Average donation    \n'
'-----------------   -----------------   -----------------   -----------------   \n'
'Frank Reynolds      $80.00               3                   $26.67               \n'
'Dee Reynolds        $125.00              2                   $62.50               \n'
'Dennis Reynolds     $60.00               2                   $30.00               \n'
'Mac McDonald        $80.00               3                   $26.67               \n'
'Charlie Kelly       $0.25                1                   $0.25                \n')
    assert out == test_string
    

def test_add_donation():
    add_donation('Frank Reynolds', 1000)
    assert donor_list['Frank Reynolds'] == [10, 20, 50, 1000]


def test_create_folder():
    new_path, now = create_folder()
    assert os.path.exists(new_path) is True


def test_write_email():
    now = datetime.datetime.now()
    write_email('testname',1000)
    assert os.path.exists(os.path.join(os.getcwd(), 'letters_' + now.strftime('%d%m%Y'), 'testname' + '_' + now.strftime('%d%m%Y') +
              '.txt'))


