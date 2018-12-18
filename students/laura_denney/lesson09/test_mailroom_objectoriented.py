#-------------------------------------------------#
# Title: Test Object Oriented Mail Room
# Dev:   LDenney
# Date:  December 13, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 10/11/18, Created MailRoom Part 1 File
#   Laura Denney, 10/12/18, Modified MailRoom Part 1 File
#   Laura Denney, 10/12/18, Started Part 2
#   Laura Denney, 10/12/18, Finished Part 2
#   Laura Denney, 10/31/18, Started MailRoom Part 3
#   Laura Denney, 11/7/18, Started MailRoom Part 4
#   Laura Denney, 11/7/18, Started Object Oriented Mail Room
#-------------------------------------------------#

from mailroom_objectoriented import *

def test_args():
    a = Donor("Laura Denney", 5, 6, 7)
    assert repr(a) == "Donor('laura denney', 5, 6, 7)"


def test_sort():
    a = Donor("Bob")
    a.append(5)
    a.append(6)
    c = Donor("Charles")
    c.append(500)
    e = Donor("Lewis")
    e.append(11)

    f = [a, c, e]
    f.sort(reverse = True)
    assert repr(f) == "[Donor('charles', 500), Donor('lewis', 11), Donor('bob', 5, 6)]"