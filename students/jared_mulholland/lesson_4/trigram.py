"""
Trigram analysis is very simple. Look at each set of three adjacent words in a document. Use the first two words of the set as a key, and remember the fact that the third word followed that key. Once you’ve finished, you know the list of individual words that can follow each two word sequence in the document. For example, given the input:
I wish I may I wish I might
You might generate:
"I wish" => ["I", "I"]
"wish I" => ["may", "might"]
"may I"  => ["wish"]
"I may"  => ["I"]
This says that the words “I wish” are twice followed by the word “I”, the words “wish I” are followed once by “may” and once by “might” and so on.
To generate new text from this analysis, choose an arbitrary word pair as a starting point. Use these to look up a random next word (using the table above) and append this new word to the text so far. This now gives you a new word pair at the end of the text, so look up a potential next word based on these. Add this to the list, and so on. In the previous example, we could start with “I may”. The only possible next word is “I”, so now we have:
I may I
The last two words are “may I”, so the next word is “wish”. We then look up “I wish”, and find our choice is constrained to another “I”.:
I may I wish I
Now we look up “wish I”, and find we have a choice. Let’s choose “may”:
I may I wish I may
Now we’re back where we started from, with “I may.” Following the same sequence, but choosing “might” this time, we get:
I may I wish I may I wish I might
It this point we stop, as no sequence starts “I might.
"""
import random

tg_dict = {"I wish": ["I","I"],"wish I": ["may","might"],"may I": ["wish"], "I may": ["I"]}

def trigram(dict):
    new_key = random.choice(list(dict.keys()))
    trigram = new_key

    while new_key in dict:    
        trigram = trigram + " " + dict[new_key][random.randint(0,len(dict[new_key])-1)]
        new_key = " ".join(trigram.split()[-2:])

    return trigram

#import sherlock and turn it to dictionary

import os
import random
import string

file_path = 'C:\\Users\\Jared\\Documents\\IntroToPython\\Self_Paced-Online\\students\\jared_mulholland\\lesson_4'
file_name = 'sherlock_short.txt'


def list_create(file_path, file_name):
    """takes text file and creates list, stripping punctuation and capitalization"""
    os.chdir(file_path)
    file_string = open(file_name)
    file_string = file_string.read()
    punct = str.maketrans("-().?!,",7*" ")
    file_string = file_string.translate(punct)
    file_string = file_string.lower().split()
    
    for f_str in file_string: 
        f_str.replace(" ","")
    return(file_string)

def dict_create(temp_list):
    """creates dict from list for use in trigram"""
    dict_temp = {}
    i = 0
    while i < len(temp_list)-3:
        if temp_list[i]+" "+temp_list[i+1] in dict_temp:
            dict_temp[temp_list[i]+" "+temp_list[i+1]].append(temp_list[i+2])            
        else:            
            dict_temp[temp_list[i]+" "+temp_list[i+1]] = [temp_list[i+2]]
        i+=1
    return(dict_temp)


def trigram_new(dict):
    """created trigram from dict starting form a random point within the dict"""
    new_key = random.choice(list(dict.keys()))
    trigram = str(new_key)

    while new_key in dict:  
        trigram = trigram + " " + dict[new_key][random.randint(0,len(dict[new_key])-1)]
        new_key = " ".join(trigram.split()[-2:])

    return trigram 


