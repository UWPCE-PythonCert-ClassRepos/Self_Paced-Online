"""Assignment 4
Kata Fourteen: Tom Swift Under Milk Wood
1/6/2019
Python 210"""


import random as r

with open('in.txt', 'r') as file:
    x = file.read()
file.close()

words = x.split()
sentence = 'whole of' #Where new string of word pairs will exist
tri_dict = {}
n = 0
for i in range(0, len(words)-2):

    seq = words[n] + ' ' + words[n + 1]
    if seq in tri_dict:
        tri_dict[seq].append(words[n + 2])
    else:
        tri_dict[seq] = [words[n + 2]]
    n += 1
sentence_words = sentence.split()
last_two = sentence_words[-2] + ' ' + sentence_words[-1]

while last_two in tri_dict:
    value = r.choice(tri_dict[last_two])
    sentence += ' ' + value
    sentence_words = sentence.split()
    last_two = sentence_words[-2] + ' ' + sentence_words[-1]

with open('out.txt', 'w') as file_out:
    file_out.write(sentence)
file_out.close()

#lookup last two words of sentence
#if word pair exists:
    #if more than one value/key
        #lookup random for number of values
    #if one value/key
        #select value
#if not exists(else) exit? or should this be in while loop?