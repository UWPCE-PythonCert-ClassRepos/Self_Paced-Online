"""Assignment 4
Kata Fourteen: Tom Swift Under Milk Wood
1/6/2019
Python 210"""


#Pre-processing------------------------------------------------------------------------

import random as r


def create_series(word_list):
    """Create a dictionary in form of {'word word',[]} from a list of words"""
    n = 0
    series_dict = {}
    for i in range(0, len(word_list) - 2):
        seq = word_list[n] + ' ' + word_list[n + 1]
        if seq in series_dict:
            series_dict[seq].append(word_list[n + 2])
        else:
            series_dict[seq] = [word_list[n + 2]]
        n += 1
    return series_dict

def first_words(seq):
    """Get first words to start off trigram given a list of words from a text."""
    main_string = ' '.join(seq)
    t = r.randint(1, len(seq)-2)
    seq_val = seq[t] + ' ' + seq[t+1]
    if main_string.count(seq_val) > 1:
        print('seq_val=', seq_val)
        return seq_val
    else:
        return first_words(seq)



#Processing------------------------------------------------------------------------

with open("in.txt", 'r+') as file:
    x = file.read()

words = x.split()

#for text cleaning
cleanup = ['  ','\'', '"','?',':',',','!','’','‘',';',' .']

sentence = first_words(words).capitalize()
print('sentence=', sentence)
#use function to create new dictionary object
tri_dict = create_series(words)

sentence_words = str(sentence).split()
last_two = sentence_words[-2] + ' ' + sentence_words[-1]

while last_two in tri_dict:
    value = r.choice(tri_dict[last_two])
    sentence += ' ' + value
    sentence_words = sentence.split()
    last_two = sentence_words[-2] + ' ' + sentence_words[-1]


with open('Out.txt', 'w+') as file_out:
    #shorten output text
    l = 0
    for word in sentence.split():
        print(word)

        for char in word:
            for c in char:
                if c in cleanup:
                    word = word.replace(char,'')
        if("." in word or l == 30):
            file_out.write(word.strip('\n')+"\n")
            l = 0
        else:
            file_out.write(word.strip('\n')+" ")
            l += 1

file_out.close()
file.close()


#Pseudo code for processing-----------------------------------------


#lookup last two words of sentence
#if word pair exists:
    #if more than one value/key
        #lookup random for number of values
    #if one value/key
        #select value
#if not exists(else) exit? or should this be in while loop?