from collections import defaultdict
from random import randint
import random
import urllib.request
import string


def clean_txt(txt):
    """
    Removes punctuation, converts text to lower and performs other one off text cleaning chores.

    {Extended description}

    Parameters:
    txt:string the text to be cleaned

    Returns:
    results: string the cleaned text
    """
    txt = txt.replace(r"\r\n", " ")
    txt = txt.replace(r"--", " ")
    txt = txt.lower()
    txt = remove_punctuation(txt)
    txt = txt.replace(r" i ", " I ")
    return txt


def remove_punctuation(txt):
    """
        Text cleaning helper function to parse each character, removing standard english punctuation.

        {Extended description}

        Parameters:
        txt:string the text to be cleaned of punctuation

        Returns:
        results: string the cleaned text
        """
    result = ""
    for c in txt:
        if c not in string.punctuation:
            result += c
    return result


def create_trigram(txt_location):
    """
        Takes a file location (either local or web) converts the text into a dictionary and returns new text

        {Extended description}

        Parameters:
        txt:string the location of the text

        Returns:
        prints results to screen
        """
    my_file = ""
    if txt_location.startswith("https:") or txt_location.startswith("http:"):
        my_file = str(urllib.request.urlopen(txt_location).read(1000))
    else:
        with open(txt_location) as outputfile:
            my_file = outputfile.read()
    print("Original Text:")
    print(my_file)
    print()
    my_file = clean_txt(my_file)
    txt_list = my_file.split()
    trigrams = []
    i = 0
    while i < len(txt_list) - 2:
        trigrams.append(list((txt_list[i], txt_list[i + 1], txt_list[i + 2])))
        i += 1
    print("Create List of Trigrams:")
    print(trigrams)
    print()
    bigram_list = []
    for item in trigrams:
        bigram_list.append(["{} {}".format(item[0], item[1]), item[2]])
    print("Create List of Bigrams to Build Dictionary Keys:")
    print(trigrams)
    print()
    d = defaultdict(list)
    for k, v in bigram_list:
        d[k].append(v)
    starting_pt = random.choice(list(d.keys()))
    print("Create a Dictionary of Keys and Values Matched From Text:")
    print(d.items())
    print()
    my_story = starting_pt + " "
    for i in range(10):
        for k, v in d.items():
            if k == starting_pt:
                rand_value = randint(0, len(v) - 1)
                # print("keys and values: {}, {}".format(k, v))
                my_story += v[rand_value] + " "
                new_key = k.split(' ', 1)[1]
                # print("new_key: ")
                # print(new_key)  # the list rearranges
                starting_pt = "{} {}".format(new_key, v[rand_value])
                # print("new starting point: " + starting_pt)
        i += 1
    print("The New Trigram Story:")
    print(my_story)


