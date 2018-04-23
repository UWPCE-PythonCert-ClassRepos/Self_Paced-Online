#!/usr/bin/env python3
#  Author/Student: Roy Tate (githubtater)

import string
import random

# variable to hold the location of the file to read. Place in current directory. Modify filename as needed.
book_to_read = './sherlock.txt'

def read_book():
    '''Reads the text of a file and returns it in a list'''
    stripped_text = []
    with open(book_to_read) as f:
        for line in f:
            line.rstrip()  # remove newline chars
            for char in line:
                line = line.replace('--', ' ')  # replace chars
                line = line.replace('-', ' ')
            words = line.split()
            for word in words:
                stripped_text.append(word)
    return stripped_text


def create_words_dict(text):
    '''Look at each set of three adjacent words in a document. Use the first two words of the
    set as a key, and remember the fact that the third word followed that key.'''
    stripped_text = ' '.join(text)
    words_dict = {}
    for count in range(0, len(stripped_text.split()) - 2):
        first_word = stripped_text.split()[count]
        second_word = stripped_text.split()[count+1]
        follow_word = stripped_text.split()[count+2]
        if (first_word, second_word) in words_dict:
            words_dict[first_word, second_word].append(follow_word)
        else:
            words_dict[first_word, second_word] = [follow_word]
    return words_dict


def build_sentence(words_dict):
    '''Build a sentence based on the word pairs in words_dict'''
    max_length = 14 # value cannot be less than min(sentence_length)
    sentence = ''
    sentence_length = random.randint(10, max_length)
    current_length = 0
    while current_length < sentence_length:
        random_selection = random.choice(list(words_dict.items()))
        first_two = ' '.join(random_selection[0])  # get the pair of words (key)
        next_word = random.choice(random_selection[1])  # select a random follow word
        sentence += first_two + ' ' + next_word + ' '
        current_length += 3

    # If there is any punctuation in the string at this time, remove it, then add a period '.'
    s = ''.join(char for char in sentence if char not in set(string.punctuation))
    s = s.rstrip().capitalize() + '.'  # unfortunately, our author only uses periods for ending sentences

    ## this code doesn't work as intended - commenting out
    # if 'i' in s:
    #     print('its in there!')
    #     s.replace(' i ', ' I ')
    return s


def main():
    # read the book/text and store in a variable
    book_text = read_book()
    count = 0
    num_sentences = int(input('Enter the number of sentences to generate: '))
    while count < num_sentences:
        # Pass the text to a function that builds a dict of values.
        trigram_sentence = build_sentence(create_words_dict(book_text))

    # finally, print the generated string
        print(trigram_sentence)
        count += 1
if __name__ == "__main__":
    main()