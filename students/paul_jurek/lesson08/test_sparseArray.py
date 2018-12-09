"""tests for spareArray"""
import pytest

from sparseArray import SparseArray


@pytest.fixture
def example_input():
    return [1, 2, 0, 0, 0, 0, 3, 0, 0, 4]

@pytest.fixture
def example_sparseArray(example_input): 
    return SparseArray(example_input)


@pytest.mark.parametrize("test_input", [
    ([1, 2, 0, 0, 0, 0, 3, 0, 0, 4]),
    ((1, 2, 0, 0, 0, 0, 3, 0, 0, 4))
])
def test_sparseArray_gets_initialized(test_input):
    """given user initialies like list,
    when they call for return
    they should get resulting list back"""
    print(test_input)
    sa = SparseArray(test_input)
    assert sa.sparse_array == {0: 1,
                            1: 2,
                            6: 3,
                            9: 4}


def test_correct_len(example_sparseArray):
    """ensures len returns virtual length for array"""
    assert len(example_sparseArray) == 10

def test_expanding_array(example_input):
    """ensures len returns virtual length for array"""
    sa = SparseArray(example_input)
    assert sa.expand_sparse_array() == example_input

@pytest.mark.parametrize("input_index, expected", [
    (0,1),
    (1,2),
    (3,0),
    (4,0),
    (6,3)
])
def test_get_item(example_sparseArray ,input_index, expected):
    """when user calls for indexed item
    the value is correctly returned"""
    assert example_sparseArray[input_index] == expected


def test_get_item_outside_index_errors(example_sparseArray):
    """when user calls index outside length, index error is raised"""
    with pytest.raises(IndexError): 
        example_sparseArray[len(example_sparseArray)]

def test_slice_returns_results(example_sparseArray):
    """when user calls a slice
    the results are returned correctly"""
    assert example_sparseArray[1:3:1] == [2,0]

def test_slice_outindex_returns_error(example_sparseArray):
    """when user calls a slice
    the results are returned correctly"""
    with pytest.raises(IndexError):
        example_sparseArray[1:50:1]

def test_set_item(example_sparseArray):
    """when users updates an index
    the resulting dict is updated"""
    example_sparseArray[0] = 11
    example_sparseArray[1] = 22
    example_sparseArray[2] = 33
    assert example_sparseArray.sparse_array == {0: 11,
                            1: 22,
                            2: 33,
                            6: 3,
                            9: 4}

def test_adding_0_doesnt_change(example_sparseArray):
    """when user adds 0 to existing 0 value, 
    sparse array doesnt change"""
    example_sparseArray[2] = 0
    assert example_sparseArray.sparse_array == {0: 1,
                            1: 2,
                            6: 3,
                            9: 4}

def test_setting_existing_value_to_zero_removes_from_array(example_sparseArray):
    """when user sets existing value to 0
    it is no longer in sparse array"""
    example_sparseArray[0] = 0
    assert example_sparseArray.sparse_array == {1: 2,
                            6: 3,
                            9: 4}

def test_append_nonzero_value(example_sparseArray):
    """when user appends a non-zero value
    the length increases and sparse array is upated"""
    orginal_lenth = len(example_sparseArray)
    example_sparseArray.append(5)
    assert len(example_sparseArray) == orginal_lenth + 1
    assert example_sparseArray.sparse_array == {0: 1,
                            1: 2,
                            6: 3,
                            9: 4,
                            10: 5}

def test_append_zero_value(example_sparseArray):
    """when user appends a zero value
    the length increases nut sparse array is not upated"""
    orginal_lenth = len(example_sparseArray)
    example_sparseArray.append(0)
    assert len(example_sparseArray) == orginal_lenth + 1
    assert example_sparseArray.sparse_array == {0: 1,
                            1: 2,
                            6: 3,
                            9: 4,}