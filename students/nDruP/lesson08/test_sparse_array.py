from sparse_array import *
import pytest


in_list = [1,2,0,0,0,0,3,0,0,4]
in_tup = (1,2,0,0,0,0,3,0,0,4)

def test_init():
    sa = SparseArray(in_list)
    sb = SparseArray(in_tup)
    
def test_len():
    sa = SparseArray(in_list)
    sb = SparseArray(in_tup)
    assert len(sa) == len(in_list)
    assert len(sb) == len(in_tup)

def test_get():
    sget = SparseArray(in_list)
    assert sget[0] == 1
    assert sget[9] == 4
    assert sget[2] == 0
    
def test_set():
    sset = SparseArray(in_list)
    sset[0] = -23
    sset[4] = 34
    assert sset[0] == -23
    assert sset[4] == 34

def test_del():
    sdel = SparseArray(in_list)
    del sdel[0]
    assert sdel[0] == 0
    del sdel[4]
    assert sdel[4] == 0

def test_append():
    sapp = SparseArray(in_list)
    sapp.append(84)
    assert sapp[10] == 84
    sapp.append(0)
    assert sapp[11] == 0

def test_call():
    scall = SparseArray(in_list)
    assert scall == in_list

def test_slice():
    sslice = SparseArray(in_list)
    assert sslice[:4] == in_list[:4]
    assert sslice[7:] == in_list[7:]
    assert sslice[::-1] == in_list[::-1]

def test_index_error():
    ser = SparseArray(in_list)
    with pytest.raises(IndexError) as neg1:
        val = ser[-1]
    with pytest.raises(IndexError) as el:
        val = ser[87]
    with pytest.raises(IndexError):
        ser[-1] = 12
    with pytest.raises(IndexError):
        ser[87] = 12
