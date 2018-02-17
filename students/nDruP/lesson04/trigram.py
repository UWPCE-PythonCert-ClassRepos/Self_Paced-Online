"""
Look at each set of 3 words in a text file.
Build a dict out of them where the first 2 words are the key and the 3rd word
is the value.
Write a new text file based on the trigrams created from the text file.
"""


import os
import random

random.seed(51)


def pull_text(read_dir, bof = None, eof = None):
    """
    Parse valid text from text file.
    """
    orig_text = open(read_dir, 'r')
    all_text = ''
    end = orig_text.tell()

    if bof:
        while bof not in orig_text.readline():
            continue

    while True:
        line = orig_text.readline()
        if (orig_text.tell() == end) or (eof and eof in line):
            break
        if line == '\n':
            all_text += line
        else:
            all_text += line[:len(line)-1] + ' '
        end = orig_text.tell()
    orig_text.close()
    return all_text


def build_trigram_dict(parsed_text):
    """
    Build trigrams from parsedtext.
    1. Take 3 words
    2. First 2 words are key, 3rd is value.
    3. Return dict of trigrams.
    Ignore multiple spaces/dashes.
    """
    trigram_dict = {}
    key_word = [None, None]
    ignore_char = [' ', '-']
    word = ''
    word_idx = 0
    for x in parsed_text:
        if x in ignore_char:
            if word != '':
                if None in key_word:
                    key_word[word_idx] = word
                    word_idx = word_idx + 1
                else:
                    bigram = key_word[0] + ' ' + key_word[1]
                    if not trigram_dict.get(bigram):
                        trigram_dict[bigram] = [word]
                    else:
                        trigram_dict[bigram] += [word]
                    key_word[0] = key_word[1]
                    key_word[1] = word
                word = ''
        else:
            word += x
    return trigram_dict

def make_story(story_dict):
    """
    Generate a story based on trigram dict.
    1. Begin at random key.
    2. Append key to story.
    3. Choose random value.
    4. Append value to story.
    5. New key is 2nd word of key+' '+value.
    If there is no value at new key, start at step 1.
    6. Return story
    """
    keys = list(story_dict.keys())
    start = int(random.random()*len(keys))
    story = ''

    story += keys[start]
    key = keys[start]
    while story_dict.get(key):
        words = story_dict.get(key)
        rand_word = int(random.random()*len(words))
        story += ' ' + words[rand_word]
        key = key[key.find(' ')+1:] + ' ' + words[rand_word]
    return story

def write_story(story, orig, directory):
    """
    Write generated story to text file.
    """
    new_story = open(os.path.join(directory, 'trigram_'+orig), 'w+')
    new_story.write(story)
    new_story.close()
    print("New story: trigram_" + orig  + " saved in " + directory)
    return


start_dir = os.getcwd()
orig_story = 'TaoTeChing.txt'
gtb_bof = "***"
gtb_eof = "End of the Project Gutenberg"
enjoy_story = None

sample_story = pull_text(os.path.join(start_dir, 'sample.txt'))
guten_story = pull_text(os.path.join(start_dir, orig_story), gtb_bof, gtb_eof)
short_story = pull_text(os.path.join(start_dir, 'sherlock_small.txt'))

parsed_story = guten_story
trigram_dict = build_trigram_dict(parsed_story)
while enjoy_story != 'y':
    enjoy_story = None
    built_story = make_story(trigram_dict)
    print(built_story)
    while enjoy_story not in ['y', 'n']:
        enjoy_story = input("Did you enjoy this story? (y/n)").lower()
write_story(built_story, orig_story, start_dir)
