"""Assignment 4
Kata Fourteen: Tom Swift Under Milk Wood
Ian Sahlberg
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

#for text cleaning
cleanup = ['  ','\'', '"','?',':',',','!','’','‘',';',' .']

#Processing------------------------------------------------------------------------

with open("sherlock_small.txt", 'r+') as file:
    x = file.read()

words = x.split()

sentence = first_words(words)
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
    #shorten output text and add '.' to end
    l = 0
    sentence = sentence.split()
    sentence[0] = sentence[0].capitalize()
    print('sentence',sentence)

    if len(sentence) >=300:
        sentence = sentence[:300]
        if '.' in sentence[299]:
            pass
        elif '.' in sentence[298]:
            pass
        else:
            sentence[299] = sentence[299] + '.'
    else:
        if '.' in sentence[len(sentence)-2]:
            pass
        elif '.' in sentence:
            pass
        else:
            sentence[len(sentence)-1] = sentence[len(sentence)-1] + '.'

    for word in sentence:
        print(word)
        #remove unwanted characters from text
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