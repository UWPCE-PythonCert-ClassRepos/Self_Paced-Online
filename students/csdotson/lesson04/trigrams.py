#!/usr/bin/env python3
# Lesson 4 - Trigrams # Be warned that these files have DOS line endings (carriage return followed by newline)
import random

ending_punctuation = [',', '.', ';', '?', '!']
other_punctuation = []
punctuation_remove = ['\n', '(', ')']  # text = text.replace('\n', ' ')

input_file_switch = {
    1: 'wish.txt',
    2: 'sherlock_small.txt'
}

input_file = input_file_switch[1]

with open(input_file, 'r') as f:
    text = f.read()
    for entry in punctuation_remove:
        text = text.replace(entry, '')
    for entry in ending_punctuation or other_punctuation:
        text = text.replace(entry, f' {entry}')
    text = text.split(' ')


text_hash = {}
for index in range(len(text) - 1):
    key = ' '.join(text[index:index+2])
    text_hash[key] = []  # text_hash = {'I may': [], 'I might': []...


for index in range(len(text)-2):
    pattern = text[index:index+2]
    text_hash[' '.join(pattern)].append(text[index+2]) # {'I wish': ['I', 'I']..


def create_trigram():
    sentence = 'wish I'
    count = 0
    while True:
        next_key = ' '.join(sentence.split(' ')[-2:])
        if text_hash[next_key] == [] or count > 100:
            break
        else:
            sentence += ' '
            sentence += text_hash[next_key][random.randint(0,len(text_hash[next_key])-1)]
            count += 1
    return(sentence)

# create_trigram() --> 'wish I may I wish I may I wish I might'
