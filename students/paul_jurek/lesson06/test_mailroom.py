"""test suite for mailroom exercise"""
import pytest 

from mailroom import *

@pytest.fixture
def donors():
    return {'Doug F': [100.00, 5.00],
          'Patty P': [1.00, 1000.00],
          'Warren B': [3000.00],
          }

def test_create_donation(donors):
    """tests that value added to specific donor
    when create donation called"""
    assert donors['Warren B'] == [3000.00]

    create_donation('Warren B', 10, donors)
    assert donors['Warren B'] == [3000.00, 10]


def test_menu_selection():
    pass