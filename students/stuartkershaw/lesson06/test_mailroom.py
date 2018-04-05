from mailroom import donors
from mailroom import compose_email
from mailroom import list_donors
from mailroom import show_donor_table
from mailroom import generate_letters

from os import listdir
from os.path import isfile, join


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


def test_show_donor_table(capsys):
    show_donor_table()
    captured = capsys.readouterr()
    assert captured.out == 'Donor Name          Total Given    Num Gifts'\
        '      Average Gift   \n'\
        '_________________________________________________________________\n'\
        'Anne Hathaway        2              10250          5125.0         \n'\
        'Geronimo Jackson     3              1800           600.0          \n'\
        'Dingo Dogson         3              550            183.33         \n'\
        'Leo Kottke           2              200            100.0          \n'\
        'Flask McCreole       1              1000           1000.0         \n'\
        'Piglet Norquist      3              65             21.67          \n'


def test_generate_letters(tmpdir, capsys):
    p = tmpdir.mkdir('sub')
    with p.as_cwd():
        generate_letters()
        captured = capsys.readouterr()
        assert captured.out == 'Letters generated: \n'\
            'Leo_Kottke.txt\n'\
            'Flask_McCreole.txt\n'\
            'Geronimo_Jackson.txt\n'\
            'Piglet_Norquist.txt\n'\
            'Dingo_Dogson.txt\n'\
            'Anne_Hathaway.txt\n'

    tempFiles = [f for f in listdir(p) if isfile(join(p, f))]
    assert tempFiles == ['Leo_Kottke.txt', 'Flask_McCreole.txt',
                         'Geronimo_Jackson.txt', 'Piglet_Norquist.txt',
                         'Dingo_Dogson.txt', 'Anne_Hathaway.txt']
