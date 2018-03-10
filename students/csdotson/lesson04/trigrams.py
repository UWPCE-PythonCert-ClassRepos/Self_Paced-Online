#!/usr/bin/env python3
# Lesson 4 - Trigrams
import random


ending_punctuation = [".", "?", "!"]
other_punctuation = [",", ";", ":"]
punctuation_remove = ["(", ")", "[", "]", '"', "#", "'"]
replace_with_space = ["\n", "--"]


input_file = input("Please enter the name of a file (with extension):\n")


with open(input_file, 'r') as f:
    text = f.read()
    for entry in punctuation_remove:
        text = text.replace(entry, '')
    for entry in replace_with_space:
        text = text.replace(entry, ' ')
    for entry in other_punctuation:
        text = text.replace(entry, f" {entry}")
    for entry in ending_punctuation:
        text = text.replace(entry, f" {entry}")
    text = text.split()


text_hash = {}
for index in range(len(text) - 1):
    key = ' '.join(text[index:index+2])
    text_hash[key] = []  # text_hash = {'I may': [], 'I might': []...


for index in range(len(text)-2):
    pattern = text[index:index+2]
    text_hash[' '.join(pattern)].append(text[index+2]) # {'I wish': ['I', 'I']..



random_starting_point = random.randint(0,len(text)-1)
story = ' '.join(text[random_starting_point:random_starting_point+2])
while True:
    next_key = ' '.join(story.split(' ')[-2:])
    if text_hash[next_key] == [] or len(story) > 500:
        story += '.'
        break
    else:
        story += ' '
        story += text_hash[next_key][random.randint(0,len(text_hash[next_key])-1)]


story = story.capitalize()
for entry in other_punctuation:
    story = story.replace(f' {entry}', entry)
for entry in ending_punctuation:
    story = story.replace(f' {entry}', entry)


word_array = story.split()
for index in range(len(word_array)-1):
    if '.' in word_array[index]:
        word_array[index+1] = word_array[index+1].capitalize()
story = ' '.join(word_array)

print("\nAnd, here's your story:\n\n", story)
