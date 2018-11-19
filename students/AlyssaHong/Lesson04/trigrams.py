"""
Author: Alyssa Hong
Date: 11/08/2018
Update:
Lesson4 Assignments > Trigrams()
"""

#!/usr/bin/env python3

import os
import random
import re

f = open("sherlock.txt",'r')
read_data = ""

while True:
    line = f.readline()
    if not line:
        break
    read_data = read_data + line.strip()+"\n"
f.close()
# print(read_data)


def make_split_data(read_data):
    """
    Read a file and return the file_text.
    Split words into a string by , . - ; ( ) " ' ! and space
    """
    split_data = re.split('[,|\.|\-|\*|\[|\]|\#|\:|\;|(\|)|\"|\'|!|\s]+',read_data)

    if split_data[-1] == '':
        del split_data[-1]

    return split_data


def make_story(pre_trigrms):
    """Make a dictionary of trigrams."""
    # print(pre_trigrms)
    word_index = {}
    for counter, word in enumerate(pre_trigrms):
        # print("=======counter, word==========",counter, word)
        if counter != (len(pre_trigrms)-2):
            if counter == 1000: break
            next_word = word + ' ' + pre_trigrms[counter+1]
            # print("=======next_word===========",next_word)
            # Check if key already exist
            existing_value = word_index.get(next_word, "no_key")
            # print("=======existing_value===============",existing_value)
            if existing_value == "no_key":
            # Adding new key and value
                word_index.update({next_word: [pre_trigrms[counter+2]]})
                # print("=======word_index.update=========", word_index)
            else:
                # Adding new value to existing key
                word_index[next_word].append(pre_trigrms[counter+2])
                # print("=======word_index[next_word]=========", word_index[next_word])
        else:
            break

    "test: first_two_words = Homes by"
    first_two_words = input("Type the first two words to make trigrams list: ")
    trigrams_list = first_two_words.split(' ')

    while trigrams_list != None:
        # Set key and find key value
        search_word = trigrams_list[-2] + ' ' + trigrams_list[-1]
        word_found = word_index.get(search_word)
        # print("=======word_found=========", word_found)
        if word_found != None:
            # Adding value to list for found key
            word_insert = random.choice(word_found)
            trigrams_list += [word_insert]
            # print("=======trigrams_list=========", trigrams_list)
        else:
            break
        # print("=======trigrams_list=========", trigrams_list)
    random_story = " ".join(trigrams_list)
    # print(random_story)
    return random_story


def write_random_story(random_story):
    writepath = 'sherlock_random.txt'
    if os.path.exists(writepath):
        mode = 'a'
    else:
        mode = 'w'

    with open(writepath, mode) as f:
        f.write(random_story)


def main():
    split_data = make_split_data(read_data)
    random_story = make_story(split_data)
    print(random_story)
    write_random_story(random_story)


if __name__ == '__main__':
    main()
