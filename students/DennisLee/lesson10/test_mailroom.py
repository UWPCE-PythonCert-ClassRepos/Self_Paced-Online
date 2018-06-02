import unittest, mailroom, mailroom_ui


class MailroomTestCase(unittest.TestCase):

    def setUp(self):
        donor_history = {
                'Red Herring': [65820.5, 31126.37, 15000, 2500],
                'Papa Smurf': [210.64, 1000, 57.86, 2804.83, 351.22, 48],
                'Pat Panda': [55324.4, 35570.53, 14920.50],
                'Karl-Heinz Berthold': [3545.2, 10579.31],
                'Mama Murphy': [156316.99, 8500.3, 12054.33, 600, 785.20],
                'Daphne Dastardly': [82]
        }
        self.coll = mailroom.DonorCollection()
        for name, amts in donor_history.items():
                self.coll.add(name, amts)        

    def tearDown(self):
        pass

    def test_challenge_100(self):
        new_coll = self.coll.challenge(3)
        self.assertEqual(new_coll['Red Herring'].donations,
                [197461.5, 93379.11, 45000, 7500])
        self.assertEqual(new_coll['Daphne Dastardly'].donations, [246.0])

    def test_challenge_200(self):
        new_coll = self.coll.challenge(3, 100, 1e12)
        self.assertEqual(new_coll['Red Herring'].donations,
                [197461.5, 93379.11, 45000, 7500])
        self.assertEqual(new_coll['Daphne Dastardly'].donations, [])

    def test_challenge_300(self):
        new_coll = self.coll.challenge(3, 0, 1000)
        self.assertEqual(new_coll['Karl-Heinz Berthold'].donations, [])
        self.assertEqual(new_coll['Papa Smurf'].donations, 
                [631.92, 3000, 173.58, 1053.66, 144.0])

    def test_challenge_400(self):
        new_coll = self.coll.challenge(3, 100, 1000)
        self.assertEqual(new_coll['Red Herring'].donations, [])
        self.assertEqual(new_coll['Mama Murphy'].donations, [1800.0, 2355.6])

    def test_projector_100(self):
        projected = dict(self.coll.projector(3, 100, 1e12))
        self.assertEqual(projected['Papa Smurf'], [631.92, 3000, 8414.49, 1053.66])
        self.assertEqual(projected['Daphne Dastardly'], [])

    def test_projector_200(self):
        projected = dict(self.coll.projector(3, 0, 1000))
        self.assertEqual(projected['Mama Murphy'], [1800, 2355.60])
        self.assertEqual(projected['Red Herring'], [])

    def test_projector_300(self):
        projected = dict(self.coll.projector(3, 100, 1000))
        self.assertEqual(projected['Mama Murphy'], [1800, 2355.60])
        self.assertEqual(projected['Pat Panda'], [])

    def test_do_all(self):
        self.input_strings = [
            '0', '01', '5', '6', '7', '8', 'a',  # Bad main menu input
            '2',  # Show initial donor history
            '1', '',
            '1', 'quit',
            '1', 'list', '',  # Show initial donors
            '1', 'list', 'quit',
            '1', 'Seymour Candy', '',
            '1', 'Seymour Candy', 'quit',
            '1', 'Seymour Candy', 'random gibberish instead of value',
            '1', 'Seymour Candy', '-34.45',
            '1', 'Seymour Candy', '0',
            '1', 'Seymour Candy', '650.25',  # Add new donor/gift
            '1', 'Seymour Candy', '2000',  # Add new donor/gift
            '1', 'Pat Panda', '',
            '1', 'Pat Panda', 'quit',
            '1', 'list', 'Pat Panda', 'five thousand',
            '1', 'list', 'Pat Panda', '-1000',
            '1', 'list', 'Pat Panda', '0.004',  
            # List donors, then add gift to existing donor
            '1', 'list', 'Pat Panda', '200.99',  
            '2',  # Show updated donor history
            '3', 'jfdasojdfsao^*&)^#$*^*#$@',
            '3', 'c:\\windows\\'
            '3', 'x:\\',
            '3', 'test',  # Save letters to relative subfolder
            '3', '',  # Save letters in current folder
            '3', 'c:\\letters',  # Save letters in absolute folder
            '3', '..',  # Save letters in parent folder (assuming not @ root)
            '4', '2',
            '4', '2 100',
            '4', '2 100 million',
            '4', 'two 100 1000',
            '4', '2 hundred 1000',
            '4', '-2 100 1000',
            '4', '0 100 1000'
            '4', '3 \t 100.01 \t 100',  # Floor > ceiling --> $0 contributions
            '4', '2 \t 0 \t 100 \tDoubling contributions under $100!',
            '4', '3 \t 50 \t 10000000000000 \tTripling contributions over $50!',
            '9'
        ]
        dui = mailroom_ui.DonorUI(self.coll)
        dui.feedback = self.mimic_input
        dui.manage_donors()

    def mimic_input(self, prompt, **kwargs):
        """Helper input function to imitate input during DonorUI testing."""
        return_value = " \t \t \t " + self.input_strings.pop(0) + " \t \t \t "
        print(f"\n[PROGRAM PROMPT]: '{prompt}'")
        print(f"[TEST RESPONSE]: '{return_value}'")
        print("\n")
        return return_value.strip()
        

if __name__ == "__main__":
    unittest.main()