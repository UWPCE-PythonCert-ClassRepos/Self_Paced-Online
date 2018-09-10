#!/usr/bin/env python3
# Lesson 4, Trigram

import random

def strip_punctuation(in_string):
    """
    Return a new version of the given string, stripped of punctionation
    """
    stripped_text = ""
    for c in in_string:
        if c in '!,.?()[]:;':
            c = ""
        stripped_text += c
    return stripped_text
    
def get_words_from_file(file):
    """
    Return an ordered list of words read from the given file
    """
    word_list = []
    f = open(file, 'r')
    while True:
        # read in each line, stripping punctuation since those characters aren't
        # aren't really part of the words
        next_line = strip_punctuation(f.readline().strip('\r'))
        if not next_line:
            break
        word_list.extend(next_line.split())
    return word_list
    
def create_trigram_dict(word_list):
    """
    Create and return a trigram dict from the given word list, which is a dict
    with a key of a two-word string and the list of words that follow it in the list
    """
    trigram_dict = dict()
    # iterate through word list, adding each word to the dict array associated with the
    # key based on the previous two words
    for i in range(len(word_list)-2):
        word_pair = " ".join(word_list[i:i+2])
        trigram_list = trigram_dict.setdefault(word_pair, [])
        if not word_list[i+2] in trigram_list:
            trigram_list.append(word_list[i+2])
    return trigram_dict
    
def create_trigram_out(trigram_dict, out_filename):
    """
    For the given trigram dict, create a new trigram based on a random key from the dict,
    and write it out to the given file name
    """
    out_file = open(out_filename, 'a')
    # get random 2-word pair to start trigram with
    next_pair = random.choice(list(trigram_dict.keys())).split(' ')
    # create the trigram key, the two words in a single string separated by a space
    next_key = "{} {}".format(next_pair[0], next_pair[1])
    # write the first pair to the file
    out_file.write(next_key + ' ')
    while next_key in trigram_dict:
        # iterate as long as the word pair key is in the trigram dict, adding the next word
        # from the trigram to the output file, and resetting the key pair to the next two words
        next_word = random.choice(trigram_dict[next_key])
        out_file.write(next_word + ' ')
        next_pair = [next_pair[1], next_word]
        next_key = "{} {}".format(next_pair[0], next_pair[1])
    # terminate file with a line feed
    out_file.write("\n")
    
if __name__ == "__main__":
    # prompt for a file name to read in
    filename = input("Enter file to read: ")
    # get the list of words in the file
    word_list = get_words_from_file(filename)
    print("found {:d} words in file {}".format(len(word_list), filename))
    # create the trigram dict for the word list
    trigram_dict = create_trigram_dict(word_list)
    print("trigram dict has {:d} entries".format(len(trigram_dict)))
    # write out the new trigram to a file with 'new_' prepended to the original file name
    out_filename = "new_"+filename
    create_trigram_out(trigram_dict, out_filename)
    print("Wrote new trigram doc to {}".format(out_filename))