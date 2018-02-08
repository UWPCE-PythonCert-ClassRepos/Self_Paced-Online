#!/usr/bin/env python3

import string
import random
from collections import defaultdict


def get_text():
    file = open("sherlock.txt", "r")
    text = file.read()
    file.close()
    return text


def get_word_list():
    text = get_text().replace('\n', ' ').lower()
    punc = string.punctuation.replace("-", "") #keep "-" in the punctuation
    table = str.maketrans({key: None for key in punc})
    new_text = text.translate(table)

    word = new_text.split()
    return word

# create a default list dictionary
word_dict = defaultdict(list, {})
words = get_word_list()

new_wordings = [] # Beginning of the new wordings
r = random.randint(0, len(words))

# Create trigrams in dictionary 'word_dict'
for i in range(len(words)-2):
    word_dict[words[i] + ' ' + words[i+1]].append(words[i+2])

def main():
    # Get the next word after the random picked word pairs
    next_word = word_dict[words[r] + ' ' + words[r+1]]

    # This creates the beginning of the 'new_wordings in a list'
    new_wordings.extend((words[r], words[r+1], next_word[0]))

    # Putting all words together starting with initial new_wordings defined above.
    # Stops the loop if there's no more next word after the chosen word pair
    while next_word != None:
        next_word = word_dict[new_wordings[-2] + ' ' + new_wordings[-1]] # Find the next word

        if next_word != []:
            new_wordings.append(next_word[0])
            # Delete that word from the list so it doesn't get used again
            word_dict[new_wordings[-2] + ' ' + new_wordings[-1]].pop(0)
        else:
            next_word = None
    # Print out the final wordings
    print(' '.join(new_wordings))

# start the script
if __name__ == "__main__":
    main()
