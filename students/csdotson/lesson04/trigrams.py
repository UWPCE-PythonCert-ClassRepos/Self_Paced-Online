#!/usr/bin/env python3
# Lesson 4 - Trigrams
import random

ENDING_PUNC = [".", "?", "!"]
OTHER_PUNC = [",", ";", ":"]
BLACK_LIST = ["(", ")", "[", "]", '"', "#", "'"]
REPLACE = ["\n", "--"]


def main():
    input_file = input("Please enter the name of a file (with extension):\n")
    text = read_file(input_file)
    story_dict = create_story_dict(text)
    story = make_story(text, story_dict)
    final_story = fix_punctuation_and_display(story)
    print("\nAnd, here's your story:\n\n", final_story)


def read_file(input_file):
    # Read input_file, scrub for punctuation, create array of words/punctuation
    with open(input_file, 'r') as f:
        text = f.read()
        for entry in BLACK_LIST:
            text = text.replace(entry, '')
        for entry in REPLACE:
            text = text.replace(entry, ' ')
        for entry in OTHER_PUNC + ENDING_PUNC:
            text = text.replace(entry, f" {entry}")
        return(text.split())


def create_story_dict(text):
    # Create dictionary needed to produce trigrams
    story_dict = {}
    for index in range(len(text) - 1):
        key = ' '.join(text[index:index+2])
        story_dict[key] = []
    for index in range(len(text)-2):
        pattern = text[index:index+2]
        story_dict[' '.join(pattern)].append(text[index+2])
    return(story_dict)


def make_story(text, story_dict):
    # Generate story from word dict
    random_starting_point = random.randint(0,len(text)-1)
    story = ' '.join(text[random_starting_point:random_starting_point+2])
    while True:
        next_key = ' '.join(story.split()[-2:])
        if story_dict[next_key] == [] or len(story) > 500:
            story += '...'
            break
        else:
            story += ' '
            story += story_dict[next_key][random.randint(0,len(story_dict[next_key])-1)]
    return(story)


def fix_punctuation_and_display(story):
    # Capitalize beginning of story, remove spacing around punctuation, capitalize after ending punctuation
    final_story = story.capitalize()
    for entry in OTHER_PUNC + ENDING_PUNC:
        final_story = final_story.replace(f' {entry}', entry)
    word_array = final_story.split()
    for index in range(len(word_array)-1):
        if '.' in word_array[index] or '!' in word_array[index] or '?' in word_array[index]:
            word_array[index+1] = word_array[index+1].capitalize()
    final_story = ' '.join(word_array)
    return(final_story)


### Execution of file if run as a script ###
if __name__ == "__main__":
    main()
