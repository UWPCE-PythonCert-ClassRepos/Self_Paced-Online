from mailroom import donors
from mailroom import compose_email
from mailroom import list_donors


def test_donors():
    assert isinstance(donors, dict) is True


def test_compose_email():
    assert compose_email('Anne Hathaway') == 'Dear Anne Hathaway, '\
        'thanks so much for your generous donation in the amount of: $6250.'


def test_list_donors(capsys):
    list_donors()
    captured = capsys.readouterr()
    assert captured.out == 'Anne Hathaway\n'\
        'Geronimo Jackson\n'\
        'Dingo Dogson\n'\
        'Leo Kottke\n'\
        'Flask McCreole\n'\
        'Piglet Norquist\n'
