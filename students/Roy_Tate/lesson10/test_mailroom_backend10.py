#!/usr/bin/python3

## Author/Student:  Roy Tate (githubtater)

import unittest
import mailroom_backend as mb
import os, os.path


class TestMailroomBackend(unittest.TestCase):
    donor_history = {'Fred Flintstonebanks': [27.14, 89.14],
                     'Wilma Willbanksstone': [150.00],
                     'Barney Rubblemcfuddle': [250, 24, 57, 175],
                     }

    def setUp(self):
        self.coll = mb.DonorCollection()
        for name, amounts in self.donor_history.items():
            for amount in self.donor_history[name]:
                self.coll.add(name, amount)

        self.test_donor = 'Barney Rubblemcfuddle'
        self.additional_donation_amt = 1999


    def test_donor_coll_instance_created(self):
        assert isinstance(self.coll, mb.DonorCollection)

    def test_donor_can_be_added(self):
        self.coll.add('Tommy Tommerson', 1400)
        self.assertIn('Tommy Tommerson', self.coll.donors)
        self.assertEqual(self.coll.donors['Tommy Tommerson'].total_donations, 1400)


    def test_str_function_returns_expected_value(self):
        self.assertEqual('Donor name: Barney Rubblemcfuddle  Donations: [250, 24, 57, 175]',
                         self.coll.donors[self.test_donor].__str__())

    def test_verify_file_is_saved(self):
        with self.assertRaises(FileNotFoundError):
            self.coll.save_emails('/asdfasd/asdfasdfasdsf')

        with self.assertRaises(PermissionError):
            self.coll.save_emails('/root/')
        cur_dir = os.getcwd()
        self.coll.save_emails(cur_dir)

        read_file = open(self.test_donor + '.txt')
        self.assertEqual(read_file.read(), str(self.coll.donors[self.test_donor].letter))
        read_file.close()
        if os.path.isfile(self.test_donor + '.txt'):
            pass
        else:
            raise FileNotFoundError

    def test_max_donations_returned(self):
        max_donation = self.coll.donors[self.test_donor].max_donation
        self.assertEqual(max_donation, 250)

    def test_total_donations_returned(self):
        total_donations = self.coll.donors[self.test_donor].total_donations
        self.assertEqual(total_donations, sum(self.donor_history[self.test_donor]))

    def test_num_gifts_returned(self):
        num_gifts = self.coll.donors[self.test_donor].num_gifts
        self.assertEqual(num_gifts, len(self.donor_history[self.test_donor]))
        self.assertEqual(num_gifts, 4)  # hard-coded for sanity check


    def test_donations_are_added(self):
        self.coll.add('Barney Rubble', self.additional_donation_amt)
        self.assertEqual(self.coll.donors['Barney Rubble'].total_donations, 1999)

    def test_print_challenge_results(self):
        self.new_coll = self.coll
        result = self.new_coll.challenge(2)
        for donor in result.donors:
            print(donor)

    def test_donations_multiplied_correctly(self):
        # Verify Wilma has one donation equal to $150
        wilma_donations = self.coll.donors['Wilma Willbanksstone'].all_donations
        self.assertEqual(sum(wilma_donations), 150)
        self.assertEqual(len(wilma_donations), 1)
        multiplier = 4
        self.challenge_coll = self.coll.challenge(multiplier)
        self.assertEqual(sum(self.challenge_coll.donors['Wilma Willbanksstone'].all_donations), 600)

    def test_donations_under_50_returned(self):
        pass


if __name__=="__main__":
    unittest.main()