#!/usr/bin/env python3

# from mailroom import efunc
import mailroom as m

def test_efunc_1():
    assert m.efunc() == 'exiting'


def test_writefile():
    content = 'This is a test\n'
    assert m.writefile('test', content) is True


def test_mail():
    assert m.mail() is True


def test_list_donors():
    # a = m.list_donors()
    # assert type(m.list_donors) is list 
    # assert m.list_donors is list 
    # assert type(a) is list 
    # assert type(a) is str
    assert m.list_donors() is True


# def test_add():
#     assert m.add() is True


#def test_add_amount():
#    assert m.add_amount('testdonor') is True

def test_report():
    assert m.report() is True
