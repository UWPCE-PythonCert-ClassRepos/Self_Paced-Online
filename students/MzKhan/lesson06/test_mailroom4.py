'''
Name: Muhammad Khan
Date: 03/20/2019
Assignment06
'''

import mailroom4 as m
import pytest as p
import os
import sys


def test_global_data():
    assert m.donors_data["Ashley Wiggins"] == [55.66,270,1000]
    for name, donation in zip(m.donors_name,m.donations):
        assert m.donors_data[name] == donation


def test_quit():
    with p.raises(SystemExit):
        assert m.quit()


def test_email_message():
    msg = """
    \rDear {:},

    \rThank you so much for your generous donation of $ {:.2f}.

    \rBest Regards,

    \r -Team"""
    for name, donation in m.donors_data.items():
        assert m.email_message(name,donation[-1]) == msg.format(name,
                                                                donation[-1])


def test_calculate_total_gift():
    for item in [items for items in m.calculate_total_gift()]:
        assert item[1] == sum(m.donors_data[item[0]][:])


def test_letter_format():

    msg = """Dear {:},

    Thank you so much for your kind donation of ${:.2f}. With that you have
    generously donated a total amount of ${:.2f} in your last {} donation(s).
    We must ensure you that your donations will be put to a very good use.

                                                        Sincerely,

                                                        -Team """
    for donor in m.calculate_total_gift():
        assert m.letter_format(*donor) == msg.format(*donor)


def test_sorted_list_desc():
    data = m.calculate_total_gift()
    assert m.sorted_list_desc()[0][1] == max([sum(data) for
                                                         data in m.donations])


def test_send_letter_everyone():
    m.send_letter_everyone()
    assert os.path.exists("Letters")
    for file in os.listdir(os.path.join("Letters")):
        donor = file[0:-15]
        assert donor in m.donors_data.keys()










