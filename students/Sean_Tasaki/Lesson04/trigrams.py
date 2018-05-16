import string
import random
# Book to parse
book_filename = 'sherlock_small.txt'
trigram_dict = {}
words_list = []
two_word_sequence = []
#with open('sherlock.txt', 'r') as file:
	#read = file.read()
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
		returns
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
	
	#loop continues while there is a matching key in the trigram_dict
	while trigram_val:
		trigram_key = (new_words[-2], new_words[-1])
		trigram_val = trigram_dict.get(trigram_key)
		
		if trigram_val:
			new_words.append(random.choice(trigram_val))


	add_period_at_end = str(new_words[-1]) + '.'
	new_words.insert(-1, add_period_at_end)
	print(' '.join(new_words[:-1]))

		
if __name__ == '__main__':
	read_file()
	create_text()


 



