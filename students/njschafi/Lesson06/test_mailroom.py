# NEIMA SCHAFI, LESSON 6 Assignment - test_mailroom
import pytest
import os
import mailroom
from mailroom import (quit, email, name_unknown,
                        name_exists, send_all, write_email, list_names)


class Test_Mailroom:

    def test_send_all(self):
        send_all()
        assert os.path.isfile('Leon_Dechino.txt')
        assert os.path.isfile('Rupert_Everton.txt')
        assert os.path.isfile('Zordon_Lagasse.txt')
        assert os.path.isfile('Kavinsky_Mega.txt')
        assert os.path.isfile('Corey_Camelot.txt')

    def test_write_email(self):
        write_email('Howard Moon', ['Howard', 'Moon'], 50)
        write_email('Vince Noir Jr', ['Vince', 'Noir', 'Jr'], 20)
        assert os.path.isfile('Vince_Noir_Jr.txt')
        assert os.path.isfile('Howard_Moon.txt')

    def test_list_names(self, capfd):
        list_names()
        out, err = capfd.readouterr()
        assert out == ('\nLIST OF DONORS\nCorey Camelot\nKavinsky Mega\n'
                        'Leon Dechino\nRupert Everton\nZordon Lagasse\n')

    def test_name_exists(self):
        name_exists('Leon Dechino', '375.00')
        # test to see if 375.00 got appended
        assert 375.00 in mailroom.donors['Leon Dechino']

    def test_name_unknown(self):
        name_unknown('Horse Malone', '800.00')
        # check to see if name and amount got added to dict
        assert 'Horse Malone' in mailroom.donors
        assert 800.00 in mailroom.donors['Horse Malone']

    def test_list_names2(self, capfd):
        # test list to see if new name is added
        list_names()
        out, err = capfd.readouterr()
        assert out == ('\nLIST OF DONORS\nCorey Camelot\nHorse Malone\n'
                        'Kavinsky Mega\nLeon Dechino\nRupert Everton\n'
                        'Zordon Lagasse\n')

    def test_send_all2(self):
        # test to see if email goes to added name
        send_all()
        assert os.path.isfile('Leon_Dechino.txt')
        assert os.path.isfile('Rupert_Everton.txt')
        assert os.path.isfile('Zordon_Lagasse.txt')
        assert os.path.isfile('Kavinsky_Mega.txt')
        assert os.path.isfile('Corey_Camelot.txt')
        assert os.path.isfile('Horse_Malone.txt')

    def test_email(self, capfd):
        email('Howard Moon', 50)
        out, err = capfd.readouterr()
        assert out == ('\nDear Howard Moon, \n\tThank you for your generous'
                        ' $50.00 donation.\n\tYou are an amazing person.'
                        ' Good job!\n')

    def test_quit(self):
        with pytest.raises(SystemExit):
            quit()
