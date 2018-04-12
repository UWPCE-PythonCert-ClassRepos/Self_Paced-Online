# Thomas Horn
# Lesson 4 - Trigram Analysis
# March 2018

################################################################################
# Trigram Analysis: look at each set of 3 adjacent words in sherlock.txt and/or
# sherlock_small.txt.
#   - First two words = key -> third word = value
#
# This starts at an arbitrary point and looks up a random next word using the
# table created with the above method.  This gives a new word pair at the end of
# the text which is used to look up a new potential word.
################################################################################

import os
import re
import random

def read_text(intext):
    """
    Creates the word pairs and associated new sentence words to build the
    trigram.

    Book will need to have punctuation and whitespace removed.
    """
    with open(intext, 'r') as infile:
        raw_text = infile.read()
        # Strip to only letters and spaces between words, then add to list.
        formatted_text = re.sub(r'\W', ' ', raw_text.strip().lower())
        text_list = list(formatted_text.split())
    return text_list


def create_trigrams_try_two(text_list):
    trigrams = {}
    # Add 3rd word to trigram pairs.  Create key entry if not already in dict.
    # TODO: learn about default dicts :(
    for i in range(len(text_list)-2):
        try:
            trigrams[(text_list[i], text_list[i+1])].append(text_list[i+2])
        except KeyError:
            trigrams[(text_list[i], text_list[i+1])] = (text_list[i+2])
        except AttributeError:
            trigrams[(text_list[i], text_list[i+1])] = (text_list[i+2])

    return trigrams
    

def make_short_story(text_list, trigrams):
    """
    Chooses an arbitrary word pair as the start from the text list (not dict).  
    Looks up a random next word according to the trigram dict.  Uses the created
    word pair to look up a potential next value from that key pair to add to the
    story.  Repeats until all key values are exhausted.

    Random choice is used to grab the 3rd word if multiple choices exist.
    """
    # Initial story words.
    start_number = random.randint(0, len(trigrams)-3)
    first_word = text_list[start_number]
    second_word = text_list[start_number+1]

    # Use the first and second word as the key to unlock a possible third word.
    trigram_key = (first_word, second_word)
    third_word = trigrams[trigram_key]
    story = f"{trigram_key[0]} {trigram_key[1]}"
    story = story + f' {third_word}'

    # Loop until we find a missing key.  For longer stories this is unrealistic
    # to output so create a count to 1000.  Remove to go on forever.
    count = 0
    while count < 1000:
        try:
            # Create new key based on second and third word just put down by 
            # advancing the indexes to the right one spot each (+1).
            first_word = second_word
            second_word = third_word
            trigram_key = (first_word, second_word)
            third_word = trigrams[trigram_key]
            story += f' {third_word}'
            count += 1
        except KeyError:
            break

    return story


if __name__ == '__main__':
    # Set book choice and call functions.
    choice = int(input("1: Small Text - 2: Big Text\n"))
    files = {
        1: 'sherlock_small.txt',
        2: 'sherlock.txt'
    }
    if choice == 1:
        intext = os.path.join(os.getcwd(), 'sherlock_small.txt')
        
    else:
        intext = os.path.join(os.getcwd(), 'sherlock.txt')

    text_list = read_text(intext)
    trigrams = create_trigrams_try_two(text_list)
    story = make_short_story(text_list, trigrams)
    print(story)


