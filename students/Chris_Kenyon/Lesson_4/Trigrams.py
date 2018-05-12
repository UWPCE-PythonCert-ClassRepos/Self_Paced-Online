#!/usr/bin/env python3

# Lesson_4 Activity 2 Trigrams

import os
import io
import string
import random

trigrams = {}

in_dir = os.getcwd()
out_dir = in_dir

book_file = "Sherlock.txt"
trigram_story_file = "Trigram_" + book_file
# set lines to start on to avoid meta data lines
bof_chars = "***"
eof_chars = "End of the Project Gutenberg"


def Read_parse_book(book, bof_chars=None, eof_chars=None):
    """Read in a text file and parse it so it can be used for trigram"""
    punctuation = (':', ';', ',', '?', '!', '.', "--")
    text = open(book, 'r')
    clean_text = ''
    endcheck = text.tell()
    # skip to start provided bof line
    if bof_chars:
        while bof_chars not in text.readline():
            continue
    # read and save file to variable
    while True:
        line = text.readline()
        if (text.tell() == endcheck) or (eof_chars and eof_chars in line):
            break
        if line == '\n':
            clean_text += line
        else:
            clean_text += line[:len(line)-1] + ' '
        endcheck = text.tell()
    text.close()
    # clean punctuation for spliting
    for p in punctuation:
        clean_text = clean_text.replace(p, ' {p} '.format(p=p))
    for par in ("(", ")"):
        clean_text = clean_text.replace(par, " ")
    return clean_text


def create_trigram_dict(parsed_book):
    """Create a trigram dictionary using 3 word groups"""
    justwords = parsed_book.split(" ")
    trigrams = {}
    keywords = [None, None]
    start_ind = 0
    for word in justwords:
        if word == "":
            continue
        if None in keywords:
            keywords[start_ind] = word
            start_ind += 1
        else:
            bi_key = keywords[0] + " " + keywords[1]
            if bi_key not in trigrams:
                trigrams[bi_key] = [word]
            else:
                trigrams[bi_key] += [word]
            keywords[0] = keywords[1]
            keywords[1] = word
    return trigrams


def create_story(story_dict, num_sentences):
    """Use the created trigram to create a new
       story with given number of sentences"""
    end_chars = ('.', '?', '!')
    punctuation = (':', ';', ',', '?', '!', '.', '"', "--")
    counter = 0
    rand_key = "word ."
    key_list = list(trigram.keys())
    # Don't start a new sentence with punctuation
    while any(word in punctuation for word in rand_key.split()):
        rand_key = random.choice(list(trigram.keys()))
    tall_tale = ''
    tall_tale += str(rand_key)
    while counter < num_sentences:
        new_word = random.choice(trigram.get(rand_key))
        if new_word in punctuation:
            tall_tale += new_word
        else:
            tall_tale += ' ' + new_word
        test_thing = rand_key.find(' ') + 1
        test_thing2 = rand_key[rand_key.find(' ')+1]
        rand_key = rand_key[rand_key.find(' ')+1:] + " " + new_word
        if new_word in end_chars:
            tall_tale += " "
            counter += 1
    return(tall_tale)


def write_to_file(story, book_name, output_fullpath):
    """ Write new trigram generated story to a text file """
    new_story = open(output_fullpath, 'w+')
    new_story.write(story)
    new_story.close()
    print("Trigram_" + book_name + " saved here: " + output_fullpath)
    return

parsed_book = Read_parse_book(os.path.join(in_dir, book_file),
                              bof_chars, eof_chars)
trigram = create_trigram_dict(parsed_book)
story = create_story(trigram, 1500)
write_to_file(story, book_file, os.path.join(out_dir, trigram_story_file))
