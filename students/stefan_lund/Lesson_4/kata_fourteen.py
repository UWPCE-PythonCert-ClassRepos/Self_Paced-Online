# python 3
# Stefan Lund
# Lesson_4
# kata_fourteen.py

import urllib.request
import random

# read text from url
def read_line_from(url_srce, starting, ending):
    """
        generator, returns a line from text when called

        url_srce: web site where utf-8 encoded text is located
        starting: start reading at this line
        ending: stop reading at this line

        line: yields a string of utf-8 encoded text, line by line
    """
    try:
        with urllib.request.urlopen(url_srce) as r:
            text = r.readline
            line = text()
            start = False
            while line != b"":
                # skip the header part
                while not start:
                    if line.startswith(starting):
                        start = True
                    else:
                        line = text()
                # stop reading when book ends, before the footer
                if line.startswith(ending):
                    line = "".encode("utf-8")
                else:
                    # skip empty lines
                    if line != "\r\n".encode("utf-8"):
                        line = line.decode("utf-8")
                        line = line.rstrip("\n")
                        yield line
                    line = text()

    except:
        print("something went wrong, read_line_from")


# following functions converts the text into a list of words, then
    # "scrubs" selected words to make more sense in the following word count
def make_list_of_words_from(string_line):
    # make a list of words from string, all in lower case
    list_of_words = string_line.lower().split()
    return list_of_words

def clean(characters, word):
    # wanted_word is a string
    wanted_word = word.strip(characters)
    return wanted_word

def clean_and_split(character_in_list, word):

    clean_word = [word]
    for char in character_in_list:
        if char in list(word):
            # print(char, word)
            if char == "-" and word.count(char) > 1:
                # split ==> [word1, '', '', ..., word2]
                words = word.split("-")
                clean_word = words[0], words[-1]
            elif char == "-" and word.count(char) == 1:
                clean_word = [word]
            else:
                # split ==> [clean_word, '']
                clean_word = [word.split(char)[0]]
                clean_word.append(char)
    for w in clean_word:
        if len(w) < 2 and w not in [".", "?", "!", ",", "i", "a"]:
            clean_word = [""]
    return clean_word

def change_if(word_list, dictionary):

    scrubbed_lst = []
    for word in word_list:
        if word in list(dictionary.keys()):
            # print(word, dictionary[word])
            word = dictionary[word]
        scrubbed_lst.append(word)
    return scrubbed_lst

def fix_tom():
    return ["Tom Swift", 2]

def fix_bumper():
    return ["professor Bumper", 2]

def fix_psb():
    return ["professor Swyington Bumper", 3]

def fix_swy():
    return ["Swyington Bumper", 2]

def fix_ned():
    return ["Ned Newton", 2]

def fix_chapter():
    return [None, 2]

def fix_mr(third_word):
    name = third_word.title()
    return ["Mr. " + name, 3]

def fix_mrs(third_word):
    name = third_word.title()
    return ["Mrs. " + name, 3]

def word_check_fix(three_words):
    """
        three_words: list of three strings
        if any one of the words_to_word dictionary keys are encountered the
            three_words list, starting from index 0, as a string
            made from the first word as in 'chapter or
            joined togeter by two or three words as in
            'Ned newton' or 'professor swyington bumper'
            the return string is modified by the fix_--- functions.
    """
    words_to_word = {"Tom swift"                    : fix_tom,
                     "professor bumper"             : fix_bumper,
                     "chapter"                      : fix_chapter,
                     "mr ."                         : fix_mr,
                     "mrs ."                        : fix_mrs,
                     "Ned newton"                   : fix_ned,
                     "professor swyington bumper"   : fix_psb,
                     "swyington bumper"             : fix_swy}

    compare_to = list(words_to_word.keys())

    compare_one_word = three_words[0]
    compare_two_words = " ".join([three_words[0], three_words[1]])
    compare_three_words = " ".join([three_words[0], three_words[1], three_words[2]])

    first_of_three_words = [compare_one_word, 1]
    for key_word in compare_to:
        if compare_one_word == key_word:
            return words_to_word[compare_one_word]()

        elif compare_two_words == key_word:
            if compare_two_words == "mr .":
                # special case, only function that requires an argument
                return words_to_word[compare_two_words](three_words[2])
            elif compare_two_words == "mrs .":
                return words_to_word[compare_two_words](three_words[2])
            return words_to_word[compare_two_words]()

        elif compare_three_words == key_word:
            return words_to_word[compare_three_words]()

    # print("first_of_three_words: ", first_of_three_words)
    return first_of_three_words

# make_list_of_all_words function, manages the above functions
def make_list_of_all_words(url_source, beginning, finish):
    """
        url_source: web site where utf-8 encoded text is located
        beginning: start reading at this line
        finish: stop reading at this line

        returns: scrubbed_word_list, list of words ready for analysis
    """
    unwanted_chars = '"\':;-'
    wanted_chars = [".", "!", "?", ",", "-"]
    special_chars_dict = {"ned": "Ned", "tom": "Tom", "tom's": "Tom's", "i": "I"}

    scrubbed_word_list = []
    three_word_list = []
    # lines is a generator
    lines = read_line_from(url_source, beginning, finish)
    # line is a string
    for line in lines:
        # word_list is a list of words
        word_list = make_list_of_words_from(line)
        # word is a str
        for word in word_list:
            # if word == 'mr.':
            #     print(word_list)
            # scrub1 is a str
            scrub1 = clean(unwanted_chars, word)
            # scrub2 is a list
            scrub2 = clean_and_split(wanted_chars, scrub1)

            if len(scrub2[0]) < 2 and scrub2[0] == "d":
                print("scrub2[0]: ", scrub2[0])

            # scrub3 is a list
            scrub3 = change_if(scrub2, special_chars_dict)

            if len(scrub3[0]) != 0:
                three_word_list.extend(scrub3)

            # make a list of strings of length 3, scrub the list and add as many
            # new words as necessary to mainatain the list as a queue with length 3
            if len(three_word_list) > 2:
                while len(three_word_list) > 2:
                    value = word_check_fix(three_word_list)
                    word, step = value[0], value[1]
                    if word is not None:
                        scrubbed_word_list.append(word)
                    three_word_list = three_word_list[step:]
    return scrubbed_word_list


# make all two-words combinations in the story, find them and the following words
# and count how many times each word appear after the two-word combination
def make_combo_word_from(word_list):

    # wanted_chars = [".", "!", "?", ","]
    combo_word_list = []
    # count = 0
    # while count < len(word_list) - 1:
    for i in range(len(word_list) - 1):
        combo = word_list[i:i + 2]
        # if combo[1] in wanted_chars:
            # combo = "".join(combo)
        #     count += 2
        # else:
        combo = " ".join(combo)
            # count += 1
        combo_word_list.append(combo)

    return combo_word_list

def make_and_populate_combo_dict(keys, word_list):

    combo_dict = {}
    keys = sorted(keys)

    # create a dictionary for all keys(=combo_words) with an empty dictionary as value
    for dict_key in keys:
        combo_dict[dict_key] = {}

    # for each key_combo_word add the words that follows and how many times this
        # combination of words appears
    for i in range(len(word_list) - 2):
        combo = word_list[i:i + 2]
        combo = " ".join(combo)
        following_word = word_list[i + 2]
        if following_word in combo_dict[combo]:
            combo_dict[combo][following_word] += 1
        else:
            combo_dict[combo][following_word] = 1

    combo_dict_s = {}
    for key in combo_dict:
        if combo_dict[key] != {}:
            combo_dict_s[key] = combo_dict[key]
    return combo_dict_s

# make a dictionary with the cumulative total count for each two-word combination
# as key, the difference from previous key to key represents a normalized
# scale that can then be used to randomly pick a word combination where it's
# probability to get picked is relative to how often it appeared in the story
def make_reversed_combo_frequency_from(combo_dict):
    """
    combo_dict: {"combo_word:{"word1":appeared_times,
                             "word2":appeared_times}"}
    return {sum(all appeared_times): combo_word1, ... etc}
        sum(all appeared_times) is a str(int)
    """
    freq_combo = {}
    for combo_word in list(combo_dict.keys()):
        sub_dict = combo_dict[combo_word]
        frequency = str(sum(sub_dict.values()))
        if frequency in freq_combo:
            freq_combo[frequency].append(combo_word)
        else:
            freq_combo[frequency] = [combo_word]
    return freq_combo

# same as above but this function is used for the value of the two-word combination
# dictionary, all words following the two-word combination in a dictionary with the
# number of times each word appeared after the two-word combination
def cumulative_frequency_as_key(frequency_word_dict):

    frequencies = list(frequency_word_dict.keys())
    cumulative_frequency = 0
    cumulative_frequency_dict = {}
    for frequency in frequencies:
        cumulative_frequency += int(frequency)
        cumulative_frequency_dict[cumulative_frequency] = frequency_word_dict[frequency]
    return cumulative_frequency_dict

# use the functions to read the text and create a new text based on the heuristics
# collected
def get_combo_word(cumulative_combo):

    # lower_limit is 1
    lower_limit = 1
    # upper_limit is the largest of the cumulative frequencies
    upper_limit = max(cumulative_combo.keys())
    # pick a random number in the space lower_limit to upper_limit
    r = random.randint(lower_limit, upper_limit)
    # find corresponding key in cumulative_combo
    random_key = min(k for k in cumulative_combo if k >= r)
    # one or more combo_words could be associated with this key
    combo_words = cumulative_combo[random_key]
    if len(combo_words) > 1:
        size = len(combo_words)
        # pick the combo_word at random, all words here have equal frequency
        # combo_words are of type list
        size = len(combo_words) - 1
        r = random.randint(0, size)
        combo_word = [combo_words[r]]
    else:
        combo_word = combo_words
    return combo_word

def get_next_word(word_key_frequency_value_dict):

    # word_key_frequency_value_dict is a dictionary with one or more words as keys
    next_word_keys = list(word_key_frequency_value_dict.keys())
    if len(next_word_keys) > 1:
        # need a cumulative frequency keys for word values
        sum_frequency = 0
        cumulative_freq_dictionary = {}
        for word, frequency in word_key_frequency_value_dict.items():
            sum_frequency += int(frequency)
            cumulative_freq_dictionary[sum_frequency] = word

        lower_limit = 1
        upper_limit = max(cumulative_freq_dictionary.keys())
        r = random.randint(lower_limit, upper_limit)
        random_key = min(k for k in cumulative_freq_dictionary if k >= r)
        next_word = cumulative_freq_dictionary[random_key]
    else:
        next_word = next_word_keys[0]

    return next_word


source = "http://www.gutenberg.org/cache/epub/499/pg499.txt"
start = "CHAPTER I\r".encode("utf-8")
# end = '"A joke?"'.encode("utf-8")
# end = '"Yes.  What you just read in that magazine'.encode("utf-8")
# end = b"Mary Nestor, a girl of Shopton, might also be mentioned."
end = b"End of the Project Gutenberg EBook"
# book_word_list: a list of every word from text in order
book_word_list = make_list_of_all_words(source, start, end)

# create a new list made up of every two word sequence,
#   a word can also be '.' or '?' or '!' or ','
book_combo_word_list = make_combo_word_from(book_word_list)
# make keys for a dictionary from this list
combo_dict_keys = set(book_combo_word_list[:-1])

# make a dictionary with keys being the combo_dict_keys and as
    # value for each key is another dictionary with the words following the
    # combo_dict_keys as key and valu is the number of times this combination
    # appears, (frequency). dict = {combo_word1:{next_word1:appeared_times,
                                             #   next_word2:appeared_times, etc}
                                #   combo_word2:{next_word1:appeared_times,
                                             #   next_word2:appeared_times, etc}etc}
combo_dict = make_and_populate_combo_dict(combo_dict_keys, book_word_list)

# dictionary with a str type number as key representing how many times the
    # combo words showing as dictionary values have appeared
frequency_combo_dict = make_reversed_combo_frequency_from(combo_dict)

# pick the starting combo word using weighted random
# to do this, modify the frequency_combo_dict, add the frequencies co the key
# represents relative size of this key to the total when all keys have been
# added up
# cumulative_frequency_combo_dict contains only the combo words
cumulative_frequency_combo_dict = cumulative_frequency_as_key(frequency_combo_dict)


story_list = []
# how many words to create in the gobbledygook story_list
story_length = 200
wanted_chars = [".", "!", "?", ","]

while len(story_list) < story_length:
    # len(story_list) evaluates first
    if len(story_list) < 1:# or not combo_dict(story_list[-2:])
        combo = get_combo_word(cumulative_frequency_combo_dict)
        # don't start the stry with '?' or '.'
        while any([char in combo[0] for char in wanted_chars]):
            combo = get_combo_word(cumulative_frequency_combo_dict)

        combo = combo[0]
        combo = combo.split()
        story_list.extend(combo)
    else:
        combo = " ".join(story_list[-2:])

        if combo in combo_dict.keys():
            next_word = get_next_word(combo_dict[combo])
            story_list.append(next_word)
        else:
            # this combo word was never in the book and is a dead end. make new combo
            combo = get_combo_word(cumulative_frequency_combo_dict)
            combo = combo[0]
            combo = combo.split()
            story_list.extend(combo)
story = ""
previous_word = "."
for word in story_list:
    if word in wanted_chars:
        story += word
    else:
        if previous_word in [".", "!", "?"]:
            word = word.title()
        story += " " + word
    previous_word = word
print(story)
