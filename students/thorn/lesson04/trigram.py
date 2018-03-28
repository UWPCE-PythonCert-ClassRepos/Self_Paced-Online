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

def create_digrams(text_list):
    """
    FOR TESTING ONLY

    Creates a list of digram tuples from the text.  
    
    Digram consist of the first word and the word following.
    Ex: ([0],[0+1])
    """
    digrams = []
    for i in range(len(text_list)):
        if i < len(text_list)-1:
            digrams.append((text_list[i], text_list[i+1]))
    return digrams    


def create_trigrams(text_list):
    """
    Creates a list of trigram tuples from the text.

    Trigrams consist of the first 2 words and the word following.
    Ex: ([0],[0+1],[0+2])
    """
    trigrams = []
    for i in range(len(text_list)-2):
        trigrams.append((text_list[i], text_list[i+1], text_list[i+2]))

    # Create set and shuffle for randomness.
    random.shuffle(trigrams)

    trigram_set = set(trigrams)
    return trigram_set


def make_short_story(trigrams):
    """
    Loops through our trigram tuples .  Sets the first word of the story to
    [2] of the chosen tuple.  Looks up if the story ends with that tuple so it 
    does not repeat words.  If it is 
    not in the already used list it writes the third word of that tuple.  Repeat for every tuple in there.
    """
    story = ''
    for tup in trigrams:
        if not story.endswith(tup[2]):
            story += f'{tup[2]} '
    # Formatting.
    story = story.capitalize()
    story += '.'
    print(story)    


def make_long_story(trigrams):
    """
    Same as above but writes the long one to a file called "sherlock_long.txt".
    """
    with open("sherlock_long.txt", 'w+') as outfile:
        story = ''
        for tup in trigrams:
            # first_word = tup[2].capitalize()
            # outfile.write(first_word)
            if not story.endswith(tup[2]):
                outfile.write(f'{tup[2]} ')



if __name__ == '__main__':
    choice = int(input("1: Small Text - 2: Big Text\n"))
    files = {
        1: make_short_story,
        2: make_long_story
    }

    if choice == 1:
        intext = os.path.join(os.getcwd(), 'sherlock_small.txt')
        text_list = read_text(intext)
        digrams = create_digrams(text_list)
        trigrams = create_trigrams(text_list)
        files[choice](trigrams)

    elif choice == 2:
        intext = os.path.join(os.getcwd(), 'sherlock.txt')
        text_list = read_text(intext)
        digrams = create_digrams(text_list)
        trigrams = create_trigrams(text_list)
        files[choice](trigrams)

