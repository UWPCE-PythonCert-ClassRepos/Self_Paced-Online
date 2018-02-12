"""
Look at each set of 3 words in a text file.
Build a dict out of them where the first 2 words are the key and the 3rd word
is the value.
Write a new text file based on the trigrams created from the text file.
"""


import os


def build_trigram_dict(read_dir, text_file):
    """
    Build trigrams from text file.
    1. read text file
    2. Take 3 words, unless 3rd starts with [' " ( ] start new key from
    or 2nd ends with [, . ? ! )]
    3. First 2 words are key, 3rd is value. No repeat values.
    4. Return dict of trigrams.
    """
    trigram_dict = {}


def make_story(trigram_dict):
    """
    Generate a story based on trigram dict.
    1. Begin at random key.
    2. Print key.
    3. Choose random value.
    4. Print value.
    5. New key is 2nd word of key+value.
    If there is no value at new key, start at step 1.
    6. Return story
    """
    story = ''
    return story

def write_story(story):
    """
    Write generated story to text file.
    """



read_dir = os.getcwd()+'/'
text_file = 'something.txt'
enjoy_story = None

trigram_dict = build_trigram_dict(read_dir, text_file)
while enjoy_story != 'y':
    story = make_story(trigram_dict)
    print(story)
    while enjoy_story not in ['y', 'n']:
        enjoy_story = input("Did you enjoy this story? (y/n)").lower()
write_story(story)
