
#!/usr/bin/env python3
"""Use a trigram algorithm to generate a couple hundred words of text"""

import copy
import random


short_path = "sherlock_small.txt"
path = "sherlock.txt"


def trigram_dict(path):
    """return a trigram dict based on the file at path"""
    with open(path, 'r') as read_file:
        book_lines = read_file.read()
    book_lines = book_lines.replace('\n\n', '\r')
    book_lines = book_lines.replace('\n', ' ')
    book_lines = book_lines.replace('\r', '\n')
    word_list = (book_lines).split(' ')
    for idx, word in enumerate(word_list):
        word += ' '
        word_list[idx] = word
    word_list = split_all_punctianion(word_list)
    trigram_dict = {}
    for idx in range(len(word_list) - 2):
        key = join_key(word_list[idx], word_list[idx + 1])
        try:
            trigram_dict[key].append(word_list[idx + 2])
        except KeyError:
            trigram_dict[key] = [word_list[idx + 2]]
    return trigram_dict
    # Only  dissadvantage of doing it this way is that "word1 word2 " and
    # "word1 word2" become different keys.
    # the decision is made earlier but I think it works out the same


join_key = "{}{}".format


def split_all_punctianion(word_list_in):
    """split words that contain while preserving word order"""
    word_list = copy.copy(word_list_in)
    split_words = []
    for idx, word in enumerate(word_list):
        if not(word.replace(' ','').isalnum()):
            split_words.append((idx, split_punctuation(word)))
    for idx, words in split_words[::-1]:
        del(word_list[idx])
        word_list[idx:idx] = words
    return word_list


def split_punctuation(string_in):
    """splits a string into strings that contain only letters or no letters

    Spaces are treated as a sperate word only when they come after punctiatnion
    This enables the trigram to start with the key ['.', ' ']
    """
    word_idx = 0
    word_list = []
    word_list.append(string_in[0])
    for idx in range(len(string_in)-1):
        char1_type = string_in[idx].isalnum() or string_in[idx] == ' '
        char2_type = string_in[idx+1].isalnum() or string_in[idx+1] == ' '
        if char1_type == char2_type:
            word_list[word_idx] += string_in[idx+1]
        else:
            word_list.append(string_in[idx+1])
            word_idx += 1
    return word_list

err_string = (
    'Checked all possibile paths and failed to produce text of the required minimum length.'
)



def trigram_text(trigram_dict, min_words = 300):
    """Attempts to generate text from the trigram dict longer than min_words"""
    first_pair = ['.', ' ']
    trigram_word_list = extend_word_list_recursive(trigram_dict, first_pair, min_words+1)
    if trigram_word_list is not None:
        trigram_text = ('').join(trigram_word_list[2:])
        return trigram_text
    else:
        key_options.pop(key_options.index(first_key))
        if len(key_options) == 0:
            return err_string

def extend_word_list_recursive(trigram_dict, current_list, min_words = 300):
    """Adds a word to the word list using the trigram dict

    Includes backtracking if a dead end is reached before min_words exceeded
    Only problem is you get recursion error when you try for long text
    """
    key = join_key(current_list[-2], current_list[-1])
    try:
        next_options = copy.copy(trigram_dict[key])
    except KeyError as E:
        return None
    while True:
        next_word = random.choice(next_options)
        try_word_list = copy.copy(current_list)
        try_word_list.append(next_word)
        final_word_list = extend_word_list_recursive(trigram_dict, try_word_list, min_words)
        if final_word_list is None:
            if len(try_word_list) > min_words:
                return try_word_list
            else:
                next_options.pop(next_options.index(next_word))
                if len(next_options) == 0:
                    return None
        else:
            return final_word_list



if __name__ == "__main__":
    trigram_dict = trigram_dict(short_path)
    print(trigram_text(trigram_dict, 300))