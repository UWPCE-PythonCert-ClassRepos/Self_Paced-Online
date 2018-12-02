"""tests the donor class"""

import pytest

from Donor import Donor

@pytest.mark.parametrize("new_donor", [Donor(firstname='Santa', lastname='Claus', id=1),
                                       Donor(id=2, firstname='', lastname='Jeff'),
                                       Donor(id=4, firstname=123, lastname=123),
                                       Donor(firstname='A', lastname='B', id=123)])
def test_donor_initiaztion(new_donor):
    """when donor is initiated
    the object is avaliable"""
    assert isinstance(new_donor, Donor)


def test_id_must_be_int():
    """when donor initiated with non-int id
    valueerror is raised"""
    with pytest.raises(ValueError):
        Donor(id='ss')


