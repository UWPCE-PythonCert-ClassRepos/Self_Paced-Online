#!/usr/bin/env python3
# Lesson 4 - Trigrams
import random

def run():
    input_file = input("Please enter the name of a file (with extension):\n")
    read_file(input_file)


def read_file(input_file):
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
        create_hash(text.split())


def create_hash(text):
    text_hash = {}
    for index in range(len(text) - 1):
        key = ' '.join(text[index:index+2])
        text_hash[key] = []
    for index in range(len(text)-2):
        pattern = text[index:index+2]
        text_hash[' '.join(pattern)].append(text[index+2])
    make_story(text, text_hash)


def make_story(text, text_hash):
    random_starting_point = random.randint(0,len(text)-1)
    story = ' '.join(text[random_starting_point:random_starting_point+2])
    while True:
        next_key = ' '.join(story.split(' ')[-2:])
        if text_hash[next_key] == [] or len(story) > 500:
            story += '...'
            break
        else:
            story += ' '
            story += text_hash[next_key][random.randint(0,len(text_hash[next_key])-1)]
    fix_punctuation_and_display(story)


def fix_punctuation_and_display(story):
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


ending_punctuation = [".", "?", "!"]
other_punctuation = [",", ";", ":"]
punctuation_remove = ["(", ")", "[", "]", '"', "#", "'"]
replace_with_space = ["\n", "--"]


### Execution of file if run as a script ###
if __name__ == "__main__":
    run()
