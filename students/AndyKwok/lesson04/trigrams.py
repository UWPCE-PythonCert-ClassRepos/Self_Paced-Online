# Description: Trigram Exercise
# Author: Andy Kwok
# Last Updated: 07/22/2018
# ChangeLog: 
# v1.0 - Initialization

import random
import re

# Read contents from file
f = open('sherlock_mid.txt')
read_data = f.read()
f.close()

# Split words into a string by , . - ; ( ) " ' ! and space
split_data = re.split('[,|\.|\-|\;|(\|)|\"|\'|!|\s]+',read_data)
# Remove '' caused by re.split
if split_data[-1] == '':
    del split_data[-1]    

# Generating dictionary
word_index = {}
for counter, word in enumerate(split_data):
    if counter != (len(split_data)-2):
        next_word = word + ' ' + split_data[counter+1]
        # Check if key already exist
        existing_value = word_index.get(next_word, ["Key_Do_not_Exists"])
        if existing_value == ["Key_Do_not_Exists"]:
            # Adding new key and value
            word_index.update({next_word: [split_data[counter+2]]})
        else:
            # Adding new value to existing key
            word_index[next_word].append(split_data[counter+2])
    else:
        break

# Seek user to intial word input
starter_word = input("Please provide two words to develop a trigram sequence> ")
trigrams_list = starter_word.split(' ')        

while trigrams_list != None:
    # Set key and find key value
    search_word = trigrams_list[-2] + ' ' + trigrams_list[-1]
    word_found = word_index.get(search_word)
    if word_found != None:
        # Adding value to list for found key
        word_insert = random.choice(word_found)
        trigrams_list += [word_insert]
    else:
        # Break from the loop when there is no matched key
        break
    
# Joining all words into a story
story = " ".join(trigrams_list)
print(story)



# Reference
'''
for show in word_index:
    print(show, word_index[show])
    
print(word_insert)
print(trigrams_list)
'''