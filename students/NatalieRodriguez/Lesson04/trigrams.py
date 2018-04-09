# Lesson 04: Trigrams
# Natalie Rodriguez
# April 7, 2018

#using small txt file excerpt from
#'Sometimes a Great Notion' by Ken Kesey.

#trigrams I will use
trigram = {
'I asked': ["her", ","],
'in a': ["wringer", "song"],
'and the': ["boys", "top", "waves"],
'and I': ["am", "faced"]
}

#file I'm using for this trigram analysis
book_excerpt = "Kesey.txt"

import re
import random


def open_excerpt(string):
#Opens, reads closes txt file
    f = open(string)
    data = f.read()
    f.close()
    return data


def ngrams(input, n):
#Reads text and makes trigrams
    input = input.split(' ')
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i + n])
    return output[:-1]


def make_grams():
    dict = {}
    text = (re.sub('[^A-Za-z]+', ' ', "{}".format(open_excerpt('Kesey.txt')))).lower()
    trigram = ngrams(text, 3)

    for i in range(len(trigram)):
        if dict.get(trigram[i][0] + ' ' + trigram[i][1], False) == False:
            dict[trigram[i][0] + ' ' + trigram[i][1]] = [trigram[i][2]]
        else:
            dict[trigram[i][0] + ' ' + trigram[i][1]].append(trigram[i][2])

    r = random.randint(0, len(trigram))
    trigram_word = trigram[r]
    new_trigram = trigram[r][-1]

    while new_trigram:
        new_trigram = dict.get(" ".join(trigram_word[-2:]), False)
        if new_trigram:
            trigram_word.append(random.choice(new_trigram))
    print(' '.join(trigram_word))


if __name__ == "__main__":
    make_grams()