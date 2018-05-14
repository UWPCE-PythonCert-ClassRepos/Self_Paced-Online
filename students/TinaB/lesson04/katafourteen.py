#!/usr/bin/env python3

import random

# book_text_file = "sherlock.txt"
#"sherlock_small.txt"
text_file = open("sherlock_small.txt", 'r')
text = text_file.read()
# first option takes text as is, second
words_in_text = text.split()
#words_in_text = text.replace('--', ' ').replace('.', '').replace(',', '').replace(
#    '"', '').replace("'", '').replace(":", ' ').replace('?', '').replace('!', '').replace('\n', ' ').replace('(', '').replace(')', '').split()
words_in_text = [str(i) for i in words_in_text]
text_file.close()
# print(words_in_text)


def create_trigram(trigram_text):
    '''Creates the trigram dictionary from text argument when called'''
    trigram_dictionary = {}
    # populates trigram by running a loop
    for tri_word in range(0, len(trigram_text)-2):
        # setdefault checks to see if key exists in dictionary and if not sets it with value of []
        trigram_dictionary.setdefault(
            '{} {}'.format(trigram_text[tri_word], trigram_text[tri_word+1]), [])

        trigram_dictionary['{} {}'.format(trigram_text[tri_word], trigram_text[tri_word+1])
                           ].append('{}'.format(trigram_text[tri_word+2]))
    #print(trigram_dictionary)
    return trigram_dictionary

if __name__ == "__main__":
    try:
        # creates and prints trigram dictionary
        trigram_dictionary = create_trigram(words_in_text)

        # creates the output
        starting_point = random.choice(list(trigram_dictionary))
        # print(starting_point)
        word_one,word_two = starting_point.split()
        output_kata = []
        # print(len(trigram_dictionary)-1)
        word_key = word_one + ' ' + word_two
        print(word_key)
        print(len(trigram_dictionary)-1)
        for word in range(0, len(trigram_dictionary)-1):
            if word_key in trigram_dictionary:
                output_kata.append(trigram_dictionary[word_key])

                next_word = random.choice(trigram_dictionary[word_key])
                word_one = word_two
                word_two = next_word
                word_key = word_one + ' ' + word_two

        print(" ".join(str(r) for v in output_kata for r in v))

    except KeyError:
        print("exception")
        print(" ".join(str(r) for v in output_kata for r in v))

        # print to file
        # with open('katafourteen_output.txt', 'w') as kata14_output:
        #kata14_output.write(' '.join(ouput_kata))
