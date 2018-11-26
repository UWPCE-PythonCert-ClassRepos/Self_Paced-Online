# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:00:48 2018

@author: dennis
"""
import re
import random

# For this kata, try implementing a trigram algorithm that generates a couple of hundred 
# words of text using a book-sized file as input. 
# Be warned that these files have DOS line endings (carriage return followed by newline).
# Steps for kata: 
# - Load story into list
# - Convert list into trigram dictionary
# - Build kata from dictionary

# Load story and create list of each word
def story_list(input_file):
    with open(input_file) as f:
        story_str = f.read()
        # Clean out periods and commas from story
        story_str = story_str.replace('.','')
        story_str = story_str.replace(',','')
        # Create list of words in story
        story_words = story_str.split()
    return story_words
    
# Convert list into trigram dictionary
def create_trigram_dict(storylist):
    trigram_dict = {}
    for i in range(len(storylist)-2):
        trigram_dict[storylist[i] + ' ' + storylist[i+1]] = storylist[i+2]
    return trigram_dict

# Create trigram output
def create_trigram_output(input_file, trigram_output, start_wordpair):
    d = create_trigram_dict(story_list(input_file))
    filter_string = start_wordpair
    # Create and open output file to write results
    with open(trigram_output, 'w') as f:
        # Write start of trigram to output file
        f.write(filter_string + ' ')
        # Perform trigram process up to 500 times to create kata of 500 or so words
        for i in range(500):
            # Test that not at end of file
            if not d.get(filter_string):
                break
            # Randomly choose dictionary value based on key (filter_string)
            random_value = random.choice([d.get(filter_string)])
            f.write(random_value + ' ')
            key_words = filter_string.split(' ')
            # Generate new key to filter by combining last word of prior key
            # and random value returned for prior key
            filter_string = str(key_words[1]) + " " + random_value


# Kata example for sherlock_small.txt, outputting to trigram_out_small.txt,
# starting with key of 'I was'            
create_trigram_output('sherlock_small.txt', 'trigram_out_small.txt', 'I was')    

# Kata example for sherlock.txt, outputting to trigram_out.txt,
# starting with key of 'with this'            
create_trigram_output('sherlock.txt', 'trigram_out.txt', 'with this')    
