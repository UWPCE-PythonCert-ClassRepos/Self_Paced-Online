"""implementin trigram problem in python"""


def build_trigram_dict(raw_text):
    pass

def test_building_dict():
        """given the example text tests building the dict"""
        example_text = 'I wish I may I wish I might'
        expected_result = {"I wish": {"I", "I"},
                           "wish I": {"may", "might"},
                           "may I": {"wish"},
                           "I may": {"I"},
                           }

        assert build_trigram_dict(example_text) == expected_result

