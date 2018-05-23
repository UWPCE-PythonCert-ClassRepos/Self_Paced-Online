import pytest
from ungraded import SparseArray


def test_SparseArray():
    sa = SparseArray([1, 2, 0, 0, 0, 0, 3, 0, 0, 4])
    assert sa.sa == [1, 2, 0, 3, 4]
    assert len(sa) == 10
    assert sa[0] == 1
    assert sa[2] == 0


def test_SparseArray_index_error():
    sa = SparseArray([1, 2, 0, 0, 0, 0, 3, 0, 0, 4])
    with pytest.raises(IndexError):
        sa[22]