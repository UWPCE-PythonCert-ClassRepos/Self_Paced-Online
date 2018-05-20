"""
Sean Tasaki
5/17/2018
Lesson04.trigrams.py
"""

import string
import random
# Book to parse
book_filename = 'sherlock.txt'
trigram_dict = {}
words_list = []
two_word_sequence = []

def read_file():
    with open(book_filename, 'r') as file:
	    read = file.read()
    for x in string.punctuation:
	    read = read.replace(x, " ")
    words_list = read.split()
    for word in words_list:
	    make_trigram(word)
	
def make_trigram(word):
    if len(two_word_sequence) < 2:
	    two_word_sequence.append(word)
	    return
    key = (two_word_sequence[0], two_word_sequence[1])
    if key in trigram_dict:
	    trigram_dict[key].append(word)
    else:
	    trigram_dict[key] = [word]
	#increment two_word_sequence []
    two_word_sequence.pop(0)
    two_word_sequence.append(word)


def create_text():
    new_words = []
    trigram_key = random.choice(list(trigram_dict))
	
    if len(trigram_dict[trigram_key]) > 1:
	    trigram_val = random.choice(trigram_dict.get(trigram_key))
		
    else:
	    trigram_val = trigram_dict.get(trigram_key)[0]

	# First three words of new_words list	
    new_words.extend((str(trigram_key[0]).title(), trigram_key[1], trigram_val))
	
	#loop outputs 200 words while there is a matching key in the trigram_dict
    count = 0
    while trigram_val and count < 200:
	    trigram_key = (new_words[-2], new_words[-1])
	    if trigram_key not in trigram_dict:
		    break
	    else:
		    trigram_val = trigram_dict.get(trigram_key)
		    new_words.append(random.choice(trigram_val))
	    count += 1

	# Add period to end of text. Not sure how to add punctuation throughout text.
    add_period_at_end = str(new_words[-1]) + '.'
    new_words.insert(-1, add_period_at_end)
    print(' '.join(new_words[:-1]))

		
if __name__ == '__main__':
    read_file()
    create_text()
 



