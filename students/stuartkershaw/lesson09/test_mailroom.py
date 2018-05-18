import pytest
from mailroom import Donor, DonorList


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
    assert str(excinfo.value) == "A positive donation value is required."

    d.add_donation(50)
    assert d.donations == [50]


def test_donor_list_add_donor():
    dl = DonorList()

    with pytest.raises(Exception) as excinfo:
        dl.add_donor()
    assert str(excinfo.value) == "add_donor() missing 1 required positional "\
                                 "argument: 'name'"
    dl.add_donor("Stuart")

    assert dl.donors["Stuart"].name == "Stuart"
    assert dl.donors["Stuart"].donations == []

    dl.add_donor("Cayce")

    assert dl.donors["Cayce"].name == "Cayce"
    assert dl.donors["Cayce"].donations == []


def test_donor_list_get_donor():
    dl = DonorList()
    dl.add_donor("Stuart")

    assert dl.get_donor("Cayce") == "Donor not found."
    assert dl.get_donor("Stuart").name == "Stuart"


def test_donor_list_get_donations():
    dl = DonorList()
    dl.add_donor("Stuart")

    assert dl.get_donations("Cayce") == "Donor not found."
    assert dl.get_donations("Stuart") == []


def test_donor_list_compose_thank_you(capsys):
    dl = DonorList()
    dl.add_donor("Stuart")

    stuart = dl.get_donor("Stuart")
    stuart.add_donation(50)

    dl.compose_thank_you(stuart)

    captured = capsys.readouterr()
    assert captured.out  == "Dear Stuart, "\
        "thanks so much for your generous donation in the amount of: $50.\n"


def test_donor_list_donor_names(capsys):
    dl = DonorList()
    dl.add_donor("Stuart")
    dl.add_donor("Cayce")

    dl.get_donor_names()

    captured = capsys.readouterr()
    assert captured.out == "Stuart\nCayce\n"


def test_donor_list_generate_rollup():
    dl = DonorList()
    dl.add_donor("Stuart")

    stuart = dl.get_donor("Stuart")

    stuart.add_donation(25)
    stuart.add_donation(50)

    assert stuart.donations == [25, 50]

    dl.generate_rollup()

    assert stuart.rollup == {"number": 2, "total": 75, "average": 37.50}
