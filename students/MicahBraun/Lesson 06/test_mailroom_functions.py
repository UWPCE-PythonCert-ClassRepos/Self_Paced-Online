# ----------------------------------------------------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: Lesson06: test_mailroom_functions.py
# PURPOSE: Unit testing mailroom.py (mailroom_refactor.py)
# DATE: 07/11/2018
#
# DESCRIPTION: This test suite was meant to be a means for debugging the mailroom_refactor.py module however the
#              suite is unsuccessful at debugging the material as I am unable to get the correct arguments to
#              work with my existing code. I could not find a workable and descriptive solution that mocked user-
#              -input that would work in my module and so ended up with a bunch of jumbled mess.
#
#              Note: mailroom_refactor.py was updated (see notes in file)
# ----------------------------------------------------------------------------------------------------------------------
import pytest
import mock
from mailroom_refactor import menu, add_donors, add_donation, thankyou, createreport, writeletters, displaylist, \
    update_list, get_directory, averagedonations


class TestMailroom():
    """
    Test Suite
    """

    @pytest.mark.skip(reason="No way of testing this function at present.")
    def test_menu(self):

        """
        Test menu behavior
        """
        # This all fails... Not sure how to get this to work the way I want it to.

        with mock.patch('mailroom_refactor.menu', return_value="a"):
            menu() == "Leaving menu..."

        with mock.patch('mailroom_refactor.menu', return_value="b"):
            assert menu() == "Leaving menu..."

        with mock.patch('mailroom_refactor.menu', return_value="c"):
            assert menu() == "Leaving menu..."

        with mock.patch('mailroom_refactor.menu', return_value="d"):
            assert menu() == "Exiting Program...[Press ENTER]"

    @pytest.mark.skip(reason="No way of testing this function at present.")
    def test_add_donors(self):
        """
        Test name addition behavior (allows for int/floats?)
        """

    @pytest.mark.skip(reason="No way of testing this function at present.")
    def test_add_donations(self):
        """
        Test for donation amounts being added to compiled list
        """


    @pytest.mark.skip(reason="No way of testing this function at present.")
    @mock.patch('module_under_test.input', create=True)
    def test_average(self, mocked_input):
        """
        Test meant to check that averages are coming out correctly
        """
        # NOTE: My tests are all over the place, I am not finding any sources that are comparable
        #       with my source code to be able to implement a mock/Magicmock to mimic user-input
        #       short of perhaps re-writing the entire thing...
        mocked_input.side_effect = [100, 4]
        result = averagedonations(100, 4)
        assert result == mocked_input




