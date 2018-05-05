#!/usr/bin/env python3

import random

# book_text_file = "sherlock.txt"
#"sherlock_small.txt"
text_file = open("sherlock_small.txt", 'r')
text = text_file.read()
# print(text)
words_in_text = text.replace('--', ' ').replace('.', '').replace(',', '').replace(
    '"', '').replace("'", '').replace(":", ' ').replace('?', '').replace('!', '').replace('\n', ' ').replace('(', '').replace(')', '').split()
words_in_text = [str(i) for i in words_in_text]
text_file.close()
# print(words_in_text)

# creates the trigram from text argument.s


def create_trigram(trigram_text):
    trigram_dictionary = {}
    for i in range(len(trigram_text)-3):
        try:
            trigram_dictionary[trigram_text[i] + ' ' +
                               trigram_text[i+1]].append(trigram_text[i+2])
        except:
            trigram_dictionary[trigram_text[i] + ' ' +
                               trigram_text[i+1]] = [trigram_text[i+2]]
    print("trigram_dictiony")
    print(trigram_dictionary)
    # Choose a random word to start building the output (less three from the input dictionary)
    starting_point = random.randint(0, len(trigram_text)-3)
    # create the output with the first two words from the random index
    word_one = trigram_text[starting_point]
    word_two = trigram_text[starting_point+1]
    word_key = trigram_text[starting_point] + \
        ' ' + trigram_text[starting_point+1]
    next_word = random.choice(trigram_dictionary[word_key])

    kata_text = word_key
#    kata_word = random.choice(trigram_dictionary[word_key])
    kata_text = kata_text + ' ' + next_word
    print("kata_text")
    print(kata_text)
    for word in range(300):
        word_one = word_two
        word_two = next_word
        if next_word != trigram_dictionary.keys()[-1]:
            word_key = word_one + ' ' + word_two
            next_word = random.choice(trigram_dictionary[word_key])
            kata_text = kata_text + ' ' + next_word

    return kata_text


if __name__ == "__main__":
    # trigram_input_text = read_in_data(book_text_file)
    print(create_trigram(words_in_text))
