#!/usr/bin/env python3
import string
import collections
import random
from collections import *

REP_MAX = 100

def read_book():
    """Read the whole book into a text string
       Arg:
            return string
        Description:
        - get the whole text of the book
        - get rid of the "\n" and replace it with space ' '
        - Make it all lower so that don't create so many words later
    """
    with open("sherlock_holmes.txt", 'r') as in_fd:
        return (in_fd.read().replace("\n", " ").lower())

def create_the_trigram():
    """ Return the list of trigram words
        - get rid of punctuation to create the new text
        - Create the word_table and return it
    """

    print ("create_the_trigram")
    trigram_dict = defaultdict(list)

    # create the text string of the book without puncs
    puncs = {any_punc: '' for any_punc in string.punctuation}
    puncs['-'] = ''  # - is replace with ' ' in puncs
    puncs_table = str.maketrans(puncs)

    book = read_book()
    book = book.translate(puncs_table)

    # create the words dictionaray
    words = book.split()
    for i in range(len(words)-2):
        trigram_dict[words[i] + ' ' + words[i+1]].append(words[i+2])

    #for k,v in trigram_dict.items(): print( k, v)
    return trigram_dict


def create_trigram_output():
    """Create the trigram_text.

    - Get a random number
    - Get the trigram_text of trigram_dict from that index_rdm_num

    """
    tri_text = list()
    tri_dict = defaultdict(list, {})
    tri_dict = create_the_trigram()

    # pick a random word
    #print ("\n\ncreate_trigram_output")
    tri_key = random.choice(list(tri_dict))  # type(tri_key) : string
    tri_val = tri_dict.get(tri_key)[0]       # type(tri_val) : list

    # update the tri_text_output
    tri_key_arr = tri_key.split()
    for each_text in tri_key_arr:
        tri_text.append(each_text)
    tri_text.append(tri_val)

    rep = 0
    while tri_key and rep < REP_MAX:
        # update the tri_key, tri_val, tri_text
        tri_key = tri_text[-2] + " " + tri_text[-1]
        if tri_key not in tri_dict:
            break
        else:
            tri_val = tri_dict.get(tri_key)[0]       # type(tri_val) : list
            tri_text.append(tri_val)

            rep += 1

    ret_str = ' '.join(tri_text)
    print (ret_str)


if __name__ == "__main__":
    create_trigram_output()
