#!/usr/bin/env python
import string
import random

def parse_line(text,last_two=[]):
    """Parse a line of text, stripping whitspace and punctuation. Return an
    ordered list of the words. Optional argument last_two is a two element list
    containing the last two words on the previous line."""

    # Split text into a list, removing spaces
    line = text.split()

    if last_two:
        # If a list of the last two characters is passed as an input, add it to
        # the beginning of the line list
        line.insert(0,last_two[0])
        line.insert(1,last_two[1])

    for i,word in enumerate(line):
        # Remove whitespace
        word = word.strip(string.whitespace)

        # Update the word in the original line list
        line[i] = word

        if i > 1:
            # For indices greater than 1, add tuples of the last two words to
            # the words dictionary
            if words.get((line[i-2],line[i-1])):
                # If the tuple is already in there, append its value
                words[(line[i-2],line[i-1])].append(word)
            else:
                # Otherwise, create a one word list
                words[(line[i-2],line[i-1])] = [word]

    # Return the last two characters of the line
    return line[-2:]

def make_trigram(start=[]):
    """Build a trigram using a two element starting list. If no starting list is
    specified, pick a random two words from the words dictionary to start."""

    if len(start) >= 300:
        # Return when the string reaches 300 words long.
        return start
    if not start:
        # If a start string is not provided, choose one at random from words
        start = list(random.choice(list(words.keys())))

    try:
        # Add a new word to the start string based on a lookup in the words
        # dictionary Call function recursively until the size limit is reached,
        # or a KeyError is raised.
        start.append(random.choice(words[tuple(start[-2:])]))
        start = make_trigram(start)
        return start

    except KeyError:
        # Return when no possible matches are found.
        return start

# Declare empty collectors
words = dict()
last_two = []

with open('sherlock.txt','r') as f:
    for line in f:
        # For each line, call the parse_line function to add words to the wonrd
        # dictionary. Pass the last two words of each line back.
        last_two = parse_line(line,last_two)
    story = make_trigram()
    # Join list of strings and add spaces between them. Print to screen.
    text_story = ' '.join(story)
    print(text_story)
f.close()
