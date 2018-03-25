#!/usr/bin/env python3

# from mailroom import efunc
import mailroom as m

def test_efunc_1():
    assert m.efunc() == 'exiting'


def test_writefile():
    content = 'This is a test'
    assert m.writefile('test', content) is True

