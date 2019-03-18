#!/usr/bin/env python3

import os.path
import mailroom
from mailroom import donor_db

def test_print_donors():
    assert mailroom.print_donors() == "Wassily Kandinsky\nJasper Johns\nMark Rothko\nRichard Serra\nYves Tanguy"

def test_generate_report():
	mylist = "\n".join(["Donor Name                | Total Given | Num Gifts | Average Gift", 
						"------------------------------------------------------------------",
						"Richard Serra              $  1475665.99          3  $   491888.66",
						"Mark Rothko                $   135353.33          1  $   135353.33",
						"Wassily Kandinsky          $    45987.47          3  $    15329.16",
						"Yves Tanguy                $     4076.42          2  $     2038.21",
						"Jasper Johns               $     3287.77          2  $     1643.88"])
	assert mailroom.generate_report() == mylist


def test_letter_text():
	text = f'Dear Jasper Johns,\n\n\tThank you for your donation of $153.34.\n\n\t\tSincerely,\n\t\t-The Mailroom'
	assert mailroom.letter_text("Jasper Johns", 153.34) == text

def test_letter_to_all():
	mailroom.letter_to_all()
	for name in donor_db.keys():
		assert os.path.isfile(name + ".txt")

def test_generate_thank_you_text():
	thanks = "\nDear John Smith,\n\nThank you so much for your donation of $56789.\n\nSincerely,\n\nThe Mailroom\n"
	assert mailroom.generate_thank_you_text("John Smith", 56789) == thanks

def test_current_donor_donation():
	mailroom.current_donor_donation("Wassily Kandinsky", 12345)
	assert donor_db["Wassily Kandinsky"][-1] == 12345

def test_new_donor_to_database():
	mailroom.new_donor_to_database("New Donor", 987)
	assert donor_db["New Donor"][0] == 987







