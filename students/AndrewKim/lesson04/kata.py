import string
import random
from collections import *

def read_book():
    with open("sherlock.txt", 'r') as in_fd:
        return (in_fd.read().replace("\n", " ").lower())


def create_trigram_words():
    trigram_dict = defaultdict(list)

    puncs = {any_punc: '' for any_punc in string.punctuation}
    puncs['-'] = ''
    puncs_table = str.maketrans(puncs)

    book = read_book()
    book = book.translate(puncs_table)

    words = book.split()
    for i in range(len(words)-2):
        trigram_dict[words[i] + ' ' + words[i+1]].append(words[i+2])
    return trigram_dict

def create_trigram_output():
    trigram_text = list()
    trigram_dict = defaultdict(list, {})
    trigram_dict = create_trigram_words()

    trigram_key = random.choice(list(trigram_dict))
    trigram_val = trigram_dict.get(trigram_key)[0]

    tri_key_arr = trigram_key.split()
    for each_text in tri_key_arr:
        trigram_text.append(each_text)
    trigram_text.append(trigram_val)

    rep = 0
    while trigram_key and rep < 100:
        trigram_key = trigram_text[-2] + " " + trigram_text[-1]
        if trigram_key not in trigram_dict:
            break
        else:
            trigram_val = trigram_dict.get(trigram_key)[0]
            trigram_text.append(trigram_val)
            rep += 1

    ret_str = ' '.join(trigram_text)
    print (ret_str)


if __name__ == "__main__":
    create_trigram_output()