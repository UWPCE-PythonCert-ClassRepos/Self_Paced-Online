import pytest
from mailroom import Donor


def test_donor_name():
    with pytest.raises(Exception) as excinfo:
        d = Donor()
    assert str(excinfo.value) == "__init__() missing 1 required positional "\
                                 "argument: 'name'"

    d = Donor("Stuart")
    assert d.name == "Stuart"

    d.name = "Stuart Kershaw"
    assert d.name == "Stuart Kershaw"


def test_donor_donation():
    d = Donor("Stuart")
    assert d.donations == []

    with pytest.raises(Exception) as excinfo:
        d.add_donation(-50)
        assert str(excinfo.value) == "A positive donation valie is required."

    d.add_donation(50)
    assert d.donations == [50]
