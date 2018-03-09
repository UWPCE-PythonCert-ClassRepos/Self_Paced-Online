#!/usr/bin/env python3
# Lesson 4 - Trigrams # Be warned that these files have DOS line endings (carriage return followed by newline)
import random

punctuation_keep = [',', '.', ';', '--', '?', '!', ' '] # White list?
punctuations_remove ['\n', '(', ')']

input_file = 'wish.txt'

with open(input_file, 'r') as f:
    text = f.read()

    text = text.replace('\n', ' ')
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace(',', ' ,')
    text = text.replace('.', ' .')
    text = text.split(' ')



text = 'I wish I may I wish I might'
text_array = text.split(' ')
# text_array = ['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might']


two_word_array = []
for index, word in enumerate(range(len(text_array) - 1)):
    two_word_array.append(text_array[index:index+2])
# two_word_array = [['I', 'wish'], ['wish', 'I'], ['I', 'may'], ['may', 'I'], ['I', 'wish'], ['wish', 'I'], ['I', 'might']]

new_array = []
for index, word in enumerate(range(len(text_array) - 1)):
    new_array.append(text_array[index] + " " + text_array[index + 1])
# new_array = ['I wish', 'wish I', 'I may', 'may I', 'I wish', 'wish I', 'I might']


text_hash = {}
for index, elem in enumerate(new_array):
    text_hash[elem] = []
# text_hash = {'I may': [], 'I might': [], 'I wish': [], 'may I': [], 'wish I': [1]}

for i in range(len(two_word_array)-1):
    pattern = text_array[i:i+2]
    text_hash[' '.join(pattern)].append(two_word_array[i+1][1])
    print(text_hash)
# text_hash =  {'I wish': ['I', 'I'], 'wish I': ['may', 'might'], 'may I': ['wish'], 'I may': ['I'], 'I might': []}





def create_trigram():
    sentence = 'wish I'
    while True: # While count < sum limit or text_hash[next_key] != []
        next_key = ' '.join(sentence.split(' ')[-2:])
        if text_hash[next_key] == []:
            break
        else:
            sentence += ' '
            sentence += text_hash[next_key][random.randint(0,len(text_hash[next_key])-1)]
    return(sentence)
# create_trigram() --> 'wish I may I wish I may I wish I might'
