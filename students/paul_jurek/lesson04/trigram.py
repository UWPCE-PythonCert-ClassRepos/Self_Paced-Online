"""implementin trigram problem in python

reference:
* https://startlearning.uw.edu/courses/course-v1:UW+PYTHON210+2018_Winter/courseware/f87a053c2b074100ab3d3812d247ec2c/f97813fb973f4813a16049ec8e06af36/
* http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/
"""
import random


def split_text(raw_text: str):
    """splits text to prepare for building trigram

    Takes in raw text string and splits into list in order.
    args:
        raw_text: string to be parsed

    returns
        list of word"""
    return raw_text.split()


def build_trigram_dict(split_text: list, output: dict={}):
    """using recursive function to build trigram dict
    output will utilize sets to capture results as values

    args:
        split_text: list of strings in order from original text
        output: dict of trigrams
    returns:
        updated dict of trigrams"""

    # mean we ran into end of string and cannot build trigram
    if len(split_text) < 3:
        return output
    else:
        new_key = " ".join([split_text[0], split_text[1]])
        if output.get(new_key):
            output.get(new_key).add(split_text[2])
        else:
            output[new_key] = set([split_text[2]])
        return build_trigram_dict(split_text[1:], output)


def build_kata(trigrams, starting_key=None, entry_limit=10):
    """builds kata out of trigrams"""

    # if no input key select random starting key
    if not starting_key:
        starting_key = random.choice(list(trigrams.keys()))

    counter = 0
    value1 = starting_key.split()[0]
    value2 = starting_key.split()[1]
    value3 = random.choice(list(trigrams[starting_key]))

    kata = " ".join([value1, value2, value3])

    while counter <= entry_limit:
        choices = trigrams.get(" ".join([value2, value3]))

        # verify a match is found
        if not choices:
            break

        random_choice = random.choice(list(choices))
        kata += " " + random_choice

        value1, value2, value3 = value2, value3, random_choice
        counter += 1
    
    return kata



def test_building_dict():
        """given the example text tests building the dict"""
        example_text = 'I wish I may I wish I might'
        expected_result = {"I wish": {"I", "I"},
                           "wish I": {"may", "might"},
                           "may I": {"wish"},
                           "I may": {"I"},
                           }
        test_split_text = split_text(example_text)

        assert build_trigram_dict(test_split_text) == expected_result


def test_split_text():
    """given a raw text string,
    when function to split is run
    correct split text is returned"""
    example_text = 'I wish I may I wish I might'

    assert split_text(example_text) == ['I', "wish", "I", "may", "I", "wish", "I", "might"]
